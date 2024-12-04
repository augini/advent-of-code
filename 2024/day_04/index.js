import fs from "fs"
import path from "path"
import process from "node:process"

const adjacentCoors = [
  [-1, -1],
  [-1, 1],
  [0, -1],
  [0, 1],
  [1, -1],
  [1, 1],
]

function part1(data) {
  const target = "XMAS"

  const rows = data.length
  const cols = data[0].length
  let count = 0

  function isValid(x, y, dx, dy) {
    for (let i = 0; i < target.length; i++) {
      const nx = x + i * dx
      const ny = y + i * dy
      if (nx < 0 || nx >= rows || ny < 0 || ny >= cols || data[nx][ny] !== target[i]) {
        return false
      }
    }
    return true
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      for (const [dx, dy] of adjacentCoors) {
        if (isValid(i, j, dx, dy)) {
          count++
        }
      }
    }
  }

  return count
}

function part2(data) {
  const rows = data.length
  const cols = data[0].length
  let count = 0

  function isValid(i, j) {
    if (data[i][j] === "A") {
      const upLeft = data?.[i - 1]?.[j - 1]
      const upRight = data?.[i - 1]?.[j + 1]

      const downLeft = data?.[i + 1]?.[j - 1]
      const downRight = data?.[i + 1]?.[j + 1]

      if (upLeft === "M" && upRight === "S" && downLeft === "M" && downRight === "S") {
        return true
      } else if (upLeft === "M" && upRight === "M" && downLeft === "S" && downRight === "S") {
        return true
      } else if (upLeft === "S" && upRight === "S" && downLeft === "M" && downRight === "M") {
        return true
      } else if (upLeft === "S" && upRight === "M" && downLeft === "S" && downRight === "M") {
        return true
      }
    }
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (isValid(i, j)) {
        count += 1
      }
    }
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
