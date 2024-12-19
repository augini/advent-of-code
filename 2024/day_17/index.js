import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  let registerMap = {
    A: 0,
    B: 0,
    C: 0,
  }
  const registers = data.slice(0, 3)
  let program = data.slice(4)[0]

  registers.forEach((register) => {
    let [instruction, x] = register.split(":")
    instruction = instruction.split(" ")[1].trim()
    registerMap[instruction] = parseInt(x.trim())
  })
  program = program.split(":")[1].trim().split(",").map(Number)
}

function part2(data) {
  // Solve part 2
  console.log("Solve part 2", data)
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
