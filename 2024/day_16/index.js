import fs from "fs"
import path from "path"
import process from "node:process"

const directions = [
  { dx: 1, dy: 0 }, // East
  { dx: 0, dy: 1 }, // South
  { dx: -1, dy: 0 }, // West
  { dx: 0, dy: -1 }, // North
]

function part1(data) {
  let start = null

  const col = data.length
  const row = data[0].length

  for (let y = 0; y < col; y++) {
    for (let x = 0; x < row; x++) {
      if (data[y][x] === "S") {
        start = { x, y }
      }
    }
  }

  const pq = []
  pq.push({ cost: 0, x: start.x, y: start.y, dir: 0 })
  const visited = new Set()

  while (pq.length > 0) {
    // Pop the node with the lowest cost
    pq.sort((a, b) => a.cost - b.cost) // Sort by cost (simple PQ)
    const { cost, x, y, dir } = pq.shift()

    if (data[y][x] === "E") {
      return cost
    }

    const stateKey = `${x},${y},${dir}`
    if (visited.has(stateKey)) continue
    visited.add(stateKey)

    // Explore all possible moves
    for (let i = 0; i < directions.length; i++) {
      const { dx, dy } = directions[i]
      const nX = x + dx
      const nY = y + dy

      // Check bounds and walls
      if (nY >= 0 && nY < col && nX >= 0 && nX < row && data[nY][nX] !== "#") {
        let newCost = cost + 1 // Moving forward costs 1
        if (i !== dir) {
          newCost += 1000 // Turning costs 1000
        }

        const newStateKey = `${nX},${nY},${i}`
        if (!visited.has(newStateKey)) {
          pq.push({ cost: newCost, x: nX, y: nY, dir: i })
        }
      }
    }
  }

  return -1
}

function part2(data) {
  console.log("NEEDS completion")
}

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
