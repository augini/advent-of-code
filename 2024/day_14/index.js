import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1

  data = data.map((row) => {
    const [pos, velocity] = row.split(" ")
    const [x, y] = pos.split("=")[1].split(",").map(Number)
    const [dx, dy] = velocity.split("=")[1].split(",").map(Number)
    return { x, y, dx, dy }
  })

  // const col = 7
  // const row = 11

  const col = 103
  const row = 101

  const len = data.length

  for (let i = 0; i < len; i++) {
    const curr = data[i]

    for (let count = 0; count < 100; count++) {
      let nx = curr.x + curr.dx
      let ny = curr.y + curr.dy

      nx = nx >= row ? nx % row : nx < 0 ? row + nx : nx
      ny = ny >= col ? ny % col : ny < 0 ? col + ny : ny

      curr.x = nx
      curr.y = ny
    }
  }

  let first = 0
  let second = 0
  let third = 0
  let fourth = 0

  for (let k = 0; k < len; k++) {
    const curr = data[k]

    const midCol = Math.floor(col / 2)
    const midRow = Math.floor(row / 2)

    const isFirst = curr.x < midRow && curr.y < midCol
    const isSecond = curr.x > midRow && curr.y < midCol
    const isThird = curr.x < midRow && curr.y > midCol
    const isFourth = curr.x > midRow && curr.y > midCol

    // console.log({ curr, isFirst, isSecond, isThird, isFourth })
    if (isFirst) first += 1
    else if (isSecond) second += 1
    else if (isThird) third += 1
    else if (isFourth) fourth += 1
  }

  return first * second * third * fourth
}

function part2(data) {
  // Solve part 2

  data = data.map((row) => {
    const [pos, velocity] = row.split(" ")
    const [x, y] = pos.split("=")[1].split(",").map(Number)
    const [dx, dy] = velocity.split("=")[1].split(",").map(Number)
    return { x, y, dx, dy }
  })

  // const col = 7
  // const row = 11

  const row = 101
  const col = 103

  const len = data.length

  for (let i = 0; i < len; i++) {
    const curr = data[i]

    for (let count = 0; count < 100000; count++) {
      let nx = curr.x + curr.dx
      let ny = curr.y + curr.dy

      nx = nx >= row ? nx % row : nx < 0 ? row + nx : nx
      ny = ny >= col ? ny % col : ny < 0 ? col + ny : ny

      curr.x = nx
      curr.y = ny

      const robotsAwayFromEdge = data.filter(({ x, y }) => 20 < x && row - 20 > x && 20 < y && col - 20 > y)

      if (robotsAwayFromEdge.length > 200) {
        break
      }
    }

    let first = 0
    let second = 0
    let third = 0
    let fourth = 0

    for (let k = 0; k < len; k++) {
      const curr = data[k]

      const midCol = Math.floor(col / 2)
      const midRow = Math.floor(row / 2)

      const isFirst = curr.x < midRow && curr.y < midCol
      const isSecond = curr.x > midRow && curr.y < midCol
      const isThird = curr.x < midRow && curr.y > midCol
      const isFourth = curr.x > midRow && curr.y > midCol

      if (isFirst) {
        first += 1
      } else if (isSecond) second += 1
      else if (isThird) third += 1
      else if (isFourth) fourth += 1
    }

    return first * second * third * fourth
  }
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
