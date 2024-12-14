import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  const parsed = []

  let machine = []
  data = data.map((line) => {
    const result = {}
    if (line.includes("Button")) {
      line = line.replace("Button", "").split(": ")
      const char = line[0].trim()
      const x = parseInt(line[1].split("+")[1])
      const y = parseInt(line[1].split("+")[2])
      result[char] = { x, y }
      machine.push(result)
      return
    } else if (line.includes("Prize")) {
      let [left, right] = line.split(":")
      right = right.split(", ")
      const x = parseInt(right[0].split("=")[1])
      const y = parseInt(right[1].split("=")[1])
      machine.push({ prize: { x, y } })
    }
    parsed.push(machine)
    machine = []
  })

  let tokens = 0

  for (let i = 0; i < parsed.length; i++) {
    const machine = parsed[i]
    if (!machine.length) {
      continue
    }
    const a = machine[0]["A"]
    const b = machine[1]["B"]
    const prize = machine[2]["prize"]

    for (let i = 0; i < 100; i++) {
      const yPos = (prize.y - i * b.y) / a.y
      const xPos = (prize.x - i * b.x) / a.x

      if (yPos === xPos) {
        tokens += xPos * 3 + i * 1
        break
      }
    }
  }
  return tokens
}

function gcdExtended(a, b) {
  let x0 = 1,
    y0 = 0,
    x1 = 0,
    y1 = 1
  while (b !== 0) {
    const q = Math.floor(a / b)
    ;[a, b] = [b, a % b]
    ;[x0, x1] = [x1, x0 - q * x1]
    ;[y0, y1] = [y1, y0 - q * y1]
  }
  return [a, x0, y0] // gcd, x, y
}
function solveMachine(a, b, prize) {
  const { x: aX, y: aY } = a
  const { x: bX, y: bY } = b
  const { x: targetX, y: targetY } = prize

  // Solve for X-axis
  const [gcdX, x0, y0] = gcdExtended(aX, bX)
  if (targetX % gcdX !== 0) return null // No solution for X

  const scaleX = targetX / gcdX
  let xA = x0 * scaleX
  let xB = y0 * scaleX

  // Solve for Y-axis
  const [gcdY, u0, v0] = gcdExtended(aY, bY)
  if (targetY % gcdY !== 0) return null // No solution for Y

  const scaleY = targetY / gcdY
  let yA = u0 * scaleY
  let yB = v0 * scaleY

  // Combine solutions to minimize tokens
  const stepX = bX / gcdX
  const stepY = bY / gcdY

  let minCost = Infinity
  for (let k = -1000000; k <= 1000000; k++) {
    const totalXA = xA + k * stepX
    const totalXB = xB - (k * aX) / gcdX
    const totalYA = yA + k * stepY
    const totalYB = yB - (k * aY) / gcdY

    if (totalXA >= 0 && totalXB >= 0 && totalYA >= 0 && totalYB >= 0) {
      const cost = 3 * totalXA + totalXB + 3 * totalYA + totalYB
      minCost = Math.min(minCost, cost)
    }
  }

  return minCost === Infinity ? null : minCost
}

function part2(data) {}

export function solve(puzzleInput) {
  // Parse the given input
  const data = puzzleInput.split(/\r?\n/)

  // Get the solutions for each problem
  const solution1 = part1(data)
  const solution2 = part2(data)

  return [solution1, solution2]
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const args = process.argv.slice(2)

  args.forEach((filePath) => {
    const puzzleInput = fs.readFileSync(path.resolve(filePath), "utf8")
    const solutions = solve(puzzleInput)
    console.log(solutions.map(String).join("\n"))
  })
}
