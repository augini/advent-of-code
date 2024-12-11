import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  data = data.map((row) => row.split(" ").map(Number)).flat()

  let nextData = data

  for (let i = 0; i < 25; i++) {
    data = nextData
    nextData = []

    for (let ind = 0; ind < data.length; ind++) {
      let curr = data[ind]
      if (curr === 0) {
        nextData.push(1)
        // If has an even number of digits, split into two
      } else if (curr?.toString().split("").length % 2 === 0) {
        const stringInt = curr?.toString().split("")
        const length = stringInt.length

        const left = parseInt(stringInt.slice(0, length / 2).join(""))
        const right = parseInt(stringInt.slice(length / 2, length).join(""))

        nextData.push(left)
        nextData.push(right)
      } else {
        nextData.push(curr * 2024)
      }
    }
  }

  return nextData.length
}

function part2(data) {
  // Solve part 2
  let freqMap = {}

  // Preprocess the data into an array of numbers
  data = data.map((row) => row.split(" ").map(Number)).flat()

  // Create the frequency map
  data.forEach((integer) => {
    freqMap[integer] = (freqMap[integer] || 0) + 1
  })

  for (let counter = 0; counter < 75; counter++) {
    let newFreqMap = {}

    for (const [key, value] of Object.entries(freqMap)) {
      if (value === 0) continue

      if (key === "0") {
        newFreqMap["1"] = (newFreqMap["1"] || 0) + value
      } else if (key.length % 2 === 0) {
        const len = key.length
        const left = parseInt(
          key
            .split("")
            .slice(0, len / 2)
            .join("")
        )
        const right = parseInt(
          key
            .split("")
            .slice(len / 2, len)
            .join("")
        )

        newFreqMap[left] = (newFreqMap[left] || 0) + value
        newFreqMap[right] = (newFreqMap[right] || 0) + value
      } else {
        const multiplied = (parseInt(key) * 2024).toString()
        newFreqMap[multiplied] = (newFreqMap[multiplied] || 0) + value
      }
    }

    freqMap = { ...newFreqMap }
  }

  return Object.values(freqMap).reduce((curr, acc) => (acc += curr), 0)
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
