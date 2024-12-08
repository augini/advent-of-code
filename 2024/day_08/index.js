import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1

  data = data.map((row) => row.split(""))
  const row = data[0].length
  const col = data.length

  const charCoordsMap = {}

  // Find unique characters and their coordinates
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (data[i][j] !== ".") {
        const curr = data[i][j]
        const existing = charCoordsMap[curr] || []
        existing.push([i, j])
        charCoordsMap[curr] = existing
      }
    }
  }

  const antinodeCoords = {}

  const updateAntinodeCoords = (y, x) => {
    if (data?.[y]?.[x]) {
      antinodeCoords[`${y},${x}`] = true
    }
  }

  // Find the diff between coords of same antenna and antinodes to existing coords
  for (const [char, coords] of Object.entries(charCoordsMap)) {
    coords.forEach((coord, i) => {
      const [y, x] = coord
      if (i + 1 < coords.length) {
        for (let k = i + 1; k < coords.length; k++) {
          const [ny, nx] = coords[k]
          const dy = y - ny
          const dx = x - nx

          const a1y = y + -2 * dy
          const a1x = x + -2 * dx
          updateAntinodeCoords(a1y, a1x)

          const a2y = ny + 2 * dy
          const a2x = nx + 2 * dx
          updateAntinodeCoords(a2y, a2x)
        }
      }
    })
  }

  return Object.keys(antinodeCoords)?.length
}

function part2(data) {
  // Solve part 1

  data = data.map((row) => row.split(""))
  const row = data[0].length
  const col = data.length

  const charCoordsMap = {}

  // Find unique characters and their coordinates
  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      if (data[i][j] !== ".") {
        const curr = data[i][j]
        const existing = charCoordsMap[curr] || []
        existing.push([i, j])
        charCoordsMap[curr] = existing
      }
    }
  }

  const antinodeCoords = {}

  const updateAntinodeCoords = (y, x) => {
    if (data?.[y]?.[x]) {
      antinodeCoords[`${y},${x}`] = true
    }
  }

  // Find the diff between coords of same antenna and antinodes to existing coords
  for (const [char, coords] of Object.entries(charCoordsMap)) {
    coords.forEach((coord, i) => {
      const [y, x] = coord

      updateAntinodeCoords(y, x)

      if (i + 1 < coords.length) {
        for (let k = i + 1; k < coords.length; k++) {
          const [ny, nx] = coords[k]

          const dy = y - ny
          const dx = x - nx

          let a1y = y - dy
          let a1x = x - dx

          if (data[a1y]?.[a1x]) {
            while (data[a1y]?.[a1x]) {
              updateAntinodeCoords(a1y, a1x)
              a1y = a1y - dy
              a1x = a1x - dx
            }
          }

          let a2y = ny + dy
          let a2x = nx + dx

          if (data[a2y]?.[a2x]) {
            while (data[a2y]?.[a2x]) {
              updateAntinodeCoords(a2y, a2x)

              a2y = a2y + dy
              a2x = a2x + dx
            }
          }
        }
      }
    })
  }

  return Object.keys(antinodeCoords)?.length
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
