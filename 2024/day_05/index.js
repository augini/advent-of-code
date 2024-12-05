import fs from "fs";
import path from "path";
import process from "node:process";

function part1(data) {
  // Solve part 1
  const emptyIndex = data.findIndex((line) => line === "");

  const rules = data.slice(0, emptyIndex).map((line) => {
    const [one, two] = line.split("|");
    return [Number(one), Number(two)];
  });

  const updates = data.slice(emptyIndex + 1);

  let sm = 0;

  const isValid = (digits) => {
    let count = 0;

    for (let i = 0; i < rules.length; i++) {
      const [one, two] = rules[i];
      const indexOne = digits.indexOf(one);
      const indexTwo = digits.indexOf(two);

      if (indexOne === -1 || indexTwo === -1 || indexOne < indexTwo) {
        count += 1;
      }
    }

    if (count === rules.length) {
      return true;
    }

    return false;
  };

  for (let i = 0; i < updates.length; i++) {
    const digits = updates[i].split(",").map(Number);
    if (isValid(digits)) {
      const len = digits.length;
      const middle = (digits.length - 1) / 2;
      sm += digits[middle];
    }
  }
  return sm;
}

function part2(data) {
  const emptyIndex = data.findIndex((line) => line === "");
  const rules = data.slice(0, emptyIndex).map((line) => {
    const [one, two] = line.split("|");
    return [Number(one), Number(two)];
  });

  const updates = data.slice(emptyIndex + 1);

  const isValid = (digits) => {
    for (let i = 0; i < rules.length; i++) {
      const [one, two] = rules[i];
      const indexOne = digits.indexOf(one);
      const indexTwo = digits.indexOf(two);

      if (indexOne !== -1 && indexTwo !== -1 && indexOne > indexTwo) {
        return false;
      }
    }
    return true;
  };

  const topologicalSort = (nodes, edges) => {
    const inDegree = new Map();
    const adjList = new Map();

    for (const node of nodes) {
      inDegree.set(node, 0);
      adjList.set(node, []);
    }

    for (const [from, to] of edges) {
      if (!nodes.includes(from) || !nodes.includes(to)) continue;
      adjList.get(from).push(to);
      inDegree.set(to, inDegree.get(to) + 1);
    }

    const queue = [];
    for (const [node, degree] of inDegree) {
      if (degree === 0) queue.push(node);
    }

    const sorted = [];
    while (queue.length > 0) {
      const current = queue.shift();
      sorted.push(current);
      for (const neighbor of adjList.get(current)) {
        inDegree.set(neighbor, inDegree.get(neighbor) - 1);
        if (inDegree.get(neighbor) === 0) queue.push(neighbor);
      }
    }

    return sorted;
  };

  let sm = 0;

  for (let i = 0; i < updates.length; i++) {
    const digits = updates[i].split(",").map(Number);

    if (!isValid(digits)) {
      const sorted = topologicalSort(digits, rules);
      const middle = Math.floor((sorted.length - 1) / 2);
      sm += sorted[middle];
    }
  }

  return sm;
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
