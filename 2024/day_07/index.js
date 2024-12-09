import fs from "fs"
import path from "path"
import process from "node:process"

const customEval = (expr) => {
  const splitPieces = expr.split("+")
  const pieces = []

  splitPieces.forEach((piece) => {
    if (piece.includes("*")) {
      const multiplications = piece.split("*")
      multiplications.forEach((digit) => {
        pieces.push(parseInt(digit))
        pieces.push("*")
      })
    } else {
      pieces.push(parseInt(piece))
      pieces.push("+")
    }
  })

  console.log({ expr, splitPieces, pieces })

  let operator = ""

  const result = pieces.reduce((acc, curr) => {
    if (curr === "+") {
      operator = "add"
    } else if (curr === "*") {
      operator = "multiply"
    } else {
      curr = parseInt(curr)

      if (!operator) {
        return curr
      } else if (operator === "add") {
        acc = acc + curr
      } else if (operator === "multiply") {
        acc = acc * curr
      }
    }
    return parseInt(acc)
  }, 0)
  return result
}

console.log({ res: customEval("2+4+2*20*10+50*20") })

function part1(data) {
  // Solve part 1
  let sm = 0

  const len = data.length
  for (let i = 0; i < len; i++) {
    let [result, equation] = data[i].split(":")
    equation = equation.trim()
    console.log({ result, equation })
  }
}

function part2(data) {
  // Solve part 2
  console.log("not solved yet")
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
