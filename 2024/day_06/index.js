import fs from "fs"
import path from "path"
import process from "node:process"
let currentDir = {
  up: [0, -1],
  down: [0, 1],
  right: [1, 0],
  left: [-1, 0],
}

let nextDir = {
  up: "right",
  right: "down",
  down: "left",
  left: "up",
}

function part1(data) {
  // Solve part 1

  let col = data[0].length // Number of columns
  let row = data.length // Number of rows

  let y = 0
  let x = 0

  let direction = "up"

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (data[i][j] === "^") {
        y = i
        x = j
      }
    }
  }

  let visited = {}
  visited[`${y},${x}`] = true

  while (x < col && y < row && x >= 0 && y >= 0) {
    const [dx, dy] = currentDir[direction]
    const ny = y + dy
    const nx = x + dx

    if (data[ny]?.[nx] === "#") {
      direction = nextDir[direction]
    } else if (!data[ny]?.[nx]) {
      break
    } else {
      y = ny
      x = nx
      visited[`${y},${x}`] = true
    }
  }
  return Object.values(visited).length
}

function part2(data) {
  // Solve part 1

  let col = data[0].length // Number of columns
  let row = data.length // Number of rows

  let y = 0
  let x = 0

  let direction = "up"

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (data[i][j] === "^") {
        y = i
        x = j
      }
    }
  }

  let visited = {}

  while (x < col && y < row && x >= 0 && y >= 0) {
    const [dx, dy] = currentDir[direction]
    const ny = y + dy
    const nx = x + dx

    if (data[ny]?.[nx] === "#") {
      direction = nextDir[direction]
    } else if (!data[ny]?.[nx]) {
      break
    } else {
      y = ny
      x = nx
      visited[`${y},${x}`] = true
    }
  }

  const coords = Object.keys(visited)

  for (let coord of coords) {
    const [y, x] = coord.split(",")

    let row = data[y]
    row = row.split("")
    row[x] = "#"
    row = row.join()
    data[y] = row
  }
  return Object.values(visited).length
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
