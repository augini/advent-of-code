import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  const regex = /mul\(\d+,\d+\)/g
  const matches = data.join().match(regex)

  if (matches) {
    // Calculate the total sum of products
    const total = matches.reduce((sum, match) => {
      // Extract the numbers from the match
      const [a, b] = match.slice(4, -1).split(",").map(Number)
      return sum + parseInt(a) * parseInt(b)
    }, 0)
    return total
  }
}

function part2(data) {
  // Solve part 2
  const regex = /do\(\)|don't\(\)|mul\(\d+,\d+\)/g

  let mulEnabled = true
  let total = 0

  // Regular expression to find valid instructions
  const tokens = data.join().match(regex)

  if (tokens) {
    for (const token of tokens) {
      if (token === "do()") {
        mulEnabled = true // Enable future mul instructions
      } else if (token === "don't()") {
        mulEnabled = false // Disable future mul instructions
      } else if (token.startsWith("mul(")) {
        if (mulEnabled) {
          // Extract the numbers from the mul instruction
          const [a, b] = token.match(/\d+/g).map(Number)
          total += a * b
        }
      }
    }
  }
  return total
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
