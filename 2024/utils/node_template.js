import fs from "fs";
import path from "path";
import process from "node:process";

function part1(data) {
  // Solve part 1
  console.log("Solve part 1", data);
}

function part2(data) {
  // Solve part 2
  console.log("Solve part 2", data);
}

export function solve(puzzleInput) {
  // Parse the given input
  const data = puzzleInput.split(/\r?\n/);

  // Get the solutions for each problem
  const solution1 = part1(data);
  const solution2 = part2(data);

  return [solution1, solution2];
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const args = process.argv.slice(2);

  args.forEach((filePath) => {
    const puzzleInput = fs.readFileSync(path.resolve(filePath), "utf8");
    const solutions = solve(puzzleInput);
    console.log(solutions.map(String).join("\n"));
  });
}
