import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1

  let schematics = []
  const length = data.length

  for (let i = 0; i < length; i += 8) {
    schematics.push(data.slice(i, i + 7))
  }

  const locks = []
  const keys = []

  schematics.forEach((pattern) => {
    const isLock = pattern[0].replace(".", "").length === 5
    const heights = []

    const row = pattern[0].length
    const column = pattern.length

    for (let r = 0; r < row; r++) {
      let count = -1
      for (let c = 0; c < column; c++) {
        if (pattern[c][r] === "#") {
          count += 1
        }
      }
      heights.push(count >= 0 ? count : 0)
    }

    if (isLock) {
      locks.push(heights)
    } else {
      keys.push(heights)
    }
  })

  let fitCount = 0

  locks.forEach((lock) => {
    keys.forEach((key) => {
      let allGood = 0
      for (let i = 0; i < 5; i++) {
        if (lock[i] + key[i] <= 5) {
          allGood += 1
        }
      }
      if (allGood === 5) {
        fitCount += 1
      }
    })
  })

  return fitCount
}

function part2(data) {
  // Solve part 2
  return 2
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
