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

  let row = data[0].length
  let col = data.length

  let y = 0
  let x = 0

  let direction = "up"

  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (data[i][j] === "^") {
        y = i
        x = j
      }
    }
  }

  let visited = {}
  visited[`${y},${x}`] = true

  while (x < row && y < col && x >= 0 && y >= 0) {
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
  // Solve part 2

  let row = data[0].length
  let col = data.length

  let y = 0
  let x = 0

  let direction = "up"

  const setStartingCoords = () => {
    for (let i = 0; i < col; i++) {
      for (let j = 0; j < row; j++) {
        if (data[i][j] === "^") {
          y = i
          x = j
        }
      }
    }
  }

  setStartingCoords()

  let visited = {}
  visited[`${y},${x}`] = true

  while (x < row && y < col && x >= 0 && y >= 0) {
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

  // y,x -> coordinate to check whether causes an infinite loop
  const causesInfiniteLoop = (checkY, checkX) => {
    let direction = "up"

    let visited = {}
    visited[`${y},${x}`] = 0

    setStartingCoords()

    while (x < row && y < col && x >= 0 && y >= 0) {
      const [dx, dy] = currentDir[direction]
      const ny = y + dy
      const nx = x + dx

      if (data[ny]?.[nx] === "#" || (ny === parseInt(checkY) && nx === parseInt(checkX))) {
        direction = nextDir[direction]
      } else if (!data[ny]?.[nx]) {
        return false
      } else {
        y = ny
        x = nx

        if (visited[`${y},${x}`] > 10) {
          return true
        }

        visited[`${y},${x}`] = (visited[`${y},${x}`] || 0) + 1
      }
    }
  }

  // Take risks 😂 but don't get stuck
  let riskyCoords = 0

  for (const key in visited) {
    const [y, x] = key.split(",")
    if (causesInfiniteLoop(y, x)) {
      riskyCoords += 1
    }
  }

  return riskyCoords
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
