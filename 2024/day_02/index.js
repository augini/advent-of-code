import fs from "fs"
import path from "path"
import process from "node:process"

function part1(data) {
  // Solve part 1
  let count = 0
  data.forEach((level) => {
    const nums = level.split(" ")
    let increasing = parseInt(nums[1]) - parseInt(nums[0]) > 0
    let isSafe = false

    let increasingCount = 0
    let decreasingCount = 0

    for (let i = 0; i < nums.length - 1; i++) {
      const diff = parseInt(nums[i + 1]) - parseInt(nums[i])
      if (increasing && diff >= 1 && diff <= 3) {
        increasingCount += 1
      } else if (diff < 0 && Math.abs(diff) >= 1 && Math.abs(diff) <= 3) {
        decreasingCount += 1
      }
    }

    isSafe = (increasing && increasingCount === nums.length - 1) || decreasingCount === nums.length - 1
    if (isSafe) {
      count += 1
    }
  })

  return count
}

function part2(data) {
  // Helper function to check if a sequence is safe
  function isSafeSequence(nums) {
    let increasing = parseInt(nums[1]) - parseInt(nums[0]) > 0
    let increasingCount = 0
    let decreasingCount = 0

    for (let i = 0; i < nums.length - 1; i++) {
      const diff = parseInt(nums[i + 1]) - parseInt(nums[i])
      if (increasing && diff >= 1 && diff <= 3) {
        increasingCount += 1
      } else if (!increasing && diff <= -1 && diff >= -3) {
        decreasingCount += 1
      } else {
        return false // Violates the safe conditions
      }
    }
    return increasing ? increasingCount === nums.length - 1 : decreasingCount === nums.length - 1
  }

  // Check safety with Problem Dampener
  let count = 0

  data.forEach((level) => {
    const nums = level.split(" ").map(Number)

    // Check if the sequence is already safe
    if (isSafeSequence(nums)) {
      count += 1
      return
    }

    // Try removing each level to see if the remaining sequence is safe
    for (let i = 0; i < nums.length; i++) {
      const modifiedNums = nums.slice(0, i).concat(nums.slice(i + 1))
      if (isSafeSequence(modifiedNums)) {
        count += 1
        return
      }
    }
  })

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
