import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  data = data[0].split("")

  const layout = []
  let isFile = true
  let fileIndex = 0

  data.forEach((char) => {
    const count = parseInt(char)

    for (let i = 0; i < count; i++) {
      layout.push(isFile ? fileIndex : ".")
    }
    if (isFile) {
      fileIndex += 1
    }
    isFile = !isFile
  })

  const layoutLength = layout.length

  for (let i = layoutLength - 1; i >= 0; i--) {
    const emptyIndex = layout.findIndex((char) => char === ".")
    const remaining = layout.slice(emptyIndex, layoutLength)

    if (remaining.every((char) => char === ".")) {
      break
    }

    if (emptyIndex === -1) {
      break
    } else {
      const tmp = layout[i]
      layout[emptyIndex] = tmp
      layout[i] = "."
    }
  }

  let checkSm = 0
  layout.forEach((char, index) => {
    if (typeof char === "number" && char) {
      checkSm += char * index
    }
  })

  return checkSm
}

// I think we can store the file system as dictionary / map
// const system = [{ isSpace:false, file:[1,1,1,1] }, { isSpace: ['.', '.'] }]

function part2(data) {
  // Solve part 1
  data = data[0].split("")

  const layout = []
  let system = []

  // Keep track of file or empty space
  let isFile = true
  let fileIndex = 0
  let portion = []

  // Store file digit or empty space size to an array
  data.forEach((char) => {
    const count = parseInt(char)

    for (let i = 0; i < count; i++) {
      layout.push(isFile ? fileIndex : ".")
      portion.push(isFile ? fileIndex : ".")
    }

    if (isFile) {
      fileIndex += 1
    }

    if (portion.length > 0) {
      system.push({ isFile, portion })
      portion = []
    }

    isFile = !isFile
  })

  const size = system.length - 1

  for (let i = size; i > 0; i--) {
    const fileToSwap = system[i]

    if (!fileToSwap?.isFile) {
      continue
    }

    const fileSize = fileToSwap.portion?.length

    const emptyIndex = system.findIndex(({ isFile = false, portion }) => !isFile && portion.length >= fileSize)

    if (emptyIndex === -1 || emptyIndex > i) {
      continue
    }

    const emptySpace = system[emptyIndex]

    if (emptySpace.portion.length === fileToSwap.portion.length) {
      const tmpPortion = fileToSwap
      system[i] = system[emptyIndex]
      system[emptyIndex] = tmpPortion
    } else {
      for (let j = 0; j < fileSize; j++) {
        emptySpace.portion[j] = fileToSwap.portion[0]
      }
      fileToSwap.portion = fileToSwap.portion.map(() => ".")

      const newPortion = emptySpace.portion

      const fileOne = {
        isFile: true,
        portion: newPortion.filter((char) => char !== "."),
      }

      const fileTwo = {
        isFile: false,
        portion: newPortion.filter((char) => char === "."),
      }

      i += 1
      system = [...system.slice(0, emptyIndex), fileOne, fileTwo, ...system.slice(emptyIndex + 1)]
    }
  }

  const systemFile = Object.values(system)
    .flat()
    .map(({ portion }) => portion)
    .flat()

  // Calculate checksum
  let checkSm = 0
  systemFile.forEach((char, index) => {
    if (typeof char === "number" && char) {
      checkSm += char * index
    }
  })

  return checkSm
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
