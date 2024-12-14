import fs from "fs"
import path from "path"
import process from "node:process"

const dirs = [
  [0, -1],
  [0, 1],
  [1, 0],
  [-1, 0],
]

function part1(data) {
  // Parse data into a grid of characters
  data = data.map((row) => row.split(""))
  const rows = data.length
  const cols = data[0]?.length || 0

  const visited = Array.from({ length: rows }, () => Array(cols).fill(false))

  let total = 0

  const dfs = (y, x, char) => {
    const stack = [[y, x]]
    visited[y][x] = true

    let area = 0
    let perimeter = 0

    while (stack.length > 0) {
      const [cy, cx] = stack.pop()
      area++

      for (const [dy, dx] of dirs) {
        const ny = cy + dy
        const nx = cx + dx

        if (ny < 0 || ny >= rows || nx < 0 || nx >= cols) {
          perimeter++
        } else if (data[ny][nx] !== char) {
          perimeter++
        } else if (!visited[ny][nx]) {
          visited[ny][nx] = true
          stack.push([ny, nx])
        }
      }
    }

    return { area, perimeter }
  }

  //Calculate the total fence price
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (!visited[i][j]) {
        const char = data[i][j]
        const { area, perimeter } = dfs(i, j, char)
        total += area * perimeter
      }
    }
  }

  return total
}

function part2(data) {
  // Parse data into a grid of characters
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
