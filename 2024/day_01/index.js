import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  let left = []
  let right = []

  data.forEach((line) => {
    const [l, r] = line.split("  ")
    left.push(parseInt(l))
    right.push(parseInt(r))
  })

  left = left.sort((a, b) => a - b)
  right = right.sort((a, b) => a - b)

  let sm = 0
  for (let i = 0; i < left.length; i++) {
    sm += Math.abs(left[i] - right[i])
  }

  return sm
}

function part2(data) {
  // Solve part 2
  let left = []
  let right = []

  data.forEach((line) => {
    const [l, r] = line.split("  ")
    left.push(parseInt(l))
    right.push(parseInt(r))
  })

  const rightByRepeatCount = {}
  right.forEach((value) => {
    rightByRepeatCount[value] = (rightByRepeatCount[value] || 0) + 1
  })

  const leftByOccurrence = []
  left.forEach((value) => {
    leftByOccurrence.push(rightByRepeatCount[value] ? value * rightByRepeatCount[value] : 0)
  })

  return leftByOccurrence.reduce((acc, value) => acc + value, 0)
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
