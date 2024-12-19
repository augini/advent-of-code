import fs from "fs"
import path from "path"
import process from "node:process"

function check(str, lst) {
  const regex = new RegExp(`^(?:${lst.join("|")})*$`)
  return regex.test(str)
}

function part1(data) {
  // Solve part 1

  let towels = data
    .slice(0, 1)[0]
    .split(",")
    .map((char) => char.trim())
  const patterns = data.slice(2)

  const len = patterns.length
  let count = 0
  for (let i = 0; i < len; i++) {
    if (check(patterns[i], towels)) {
      count += 1
    }
  }

  return count
}

function part2(data) {
  const towels = new Set(data[0].split(",").map((char) => char.trim()))
  const patterns = new Set(data.slice(2))
  const memo = new Map()

  let count = 0

  function findVariations(current) {
    if (memo.has(current)) return memo.get(current)

    let localCount = 0
    for (let j = 1; j <= current.length; j++) {
      const slice = current.slice(0, j)

      if (towels.has(slice)) {
        const remaining = current.slice(j)

        if (remaining === "") {
          localCount++ // Found a valid pattern
        } else {
          localCount += findVariations(remaining)
        }
      }
    }

    memo.set(current, localCount)
    return localCount
  }

  for (const pattern of patterns) {
    count += findVariations(pattern)
  }

  return count
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
