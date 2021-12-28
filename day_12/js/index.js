const create_adjacency_list = (map) => {
  const edges = map.split("\n");
  const adjacency_list = {};

  for (let i = 0; i < edges.length; i++) {
    const [first, second] = edges[i].split("-");
    if (!adjacency_list[first]) adjacency_list[first] = [];
    if (second !== "end" && !adjacency_list[second])
      adjacency_list[second] = [];
  }

  for (let i = 0; i < edges.length; i++) {
    const [first, second] = edges[i].split("-");
    if (!adjacency_list[first].includes(second) && second !== "start")
      adjacency_list[first].push(second);

    if (
      second !== "end" &&
      !adjacency_list[second].includes(first) &&
      first !== "start"
    )
      adjacency_list[second].push(first);
  }

  return adjacency_list;
};

// {
//   start: [ 'A', 'b' ],
//   A: [ 'c', 'b', 'end' ],
//   b: [ 'A', 'd', 'end' ],
//   c: [ 'A' ],
//   d: [ 'b' ]
// }

function getLastValue(set) {
  let value;
  for (value of set);
  return value;
}

// depth first search
const find_paths = (graph, start, path) => {
  const collection = [];
  const visited_small = new Set();
  const stack = [start];

  while (stack.length > 0) {
    const current_cave = stack.pop();

    // if (path[path.length - 1] === current_cave) {
    //   path = path.slice(0, 1);
    //   visited_small.clear();
    // }

    if (current_cave === current_cave.toUpperCase()) {
      // console.log(current_cave, path, stack);
      path.push(current_cave);
    } else {
      if (!visited_small.has(current_cave)) {
        path.push(current_cave);
        visited_small.add(current_cave);
      } else {
        const lastItem = path[path.length - 1];
        if (lastItem === lastItem.toLowerCase()) {
          path.pop();
        }
        continue;
      }
    }

    if (current_cave === "end") {
      // console.log(current_cave, path, stack, visited_small);
      collection.push(path.join(","));
      path.pop();
      visited_small.delete("end");
    } else {
      graph[current_cave].forEach((cave) => stack.push(cave));
    }
  }

  return collection;
};

const graph = create_adjacency_list(`EO-jc
end-tm
jy-FI
ek-EO
mg-ek
jc-jy
FI-start
jy-mg
mg-FI
jc-tm
end-EO
ds-EO
jy-start
tm-EO
mg-jc
ek-jc
tm-ek
FI-jc
jy-EO
ek-jy
ek-LT
start-mg`);

console.log(graph);

// PART 1
// create breadth first search
const find_paths_bfs = (graph, start, path) => {
  const collection = [];

  const queue = [{ start: "" }];

  while (queue.length > 0) {
    const temp = queue.shift();

    const current_cave = Object.keys(temp)[0];
    const current_path = Object.values(temp)[0];

    if (current_cave === current_cave.toUpperCase()) {
      path.push(`${current_path},${current_cave}`);

      // if it is a small cave, check if it has been visited before
      // if not, add it to path
    } else {
      let path_array = current_path.split(",");

      if (!path_array.includes(current_cave)) {
        path.push(
          current_cave === "start"
            ? `${current_cave}`
            : `${current_path},${current_cave}`
        );

        // if it has been visited before, do not add it to path
      } else {
        const lastItem = path[path.length - 1];
        if (lastItem === lastItem.toLowerCase()) path.pop();
        continue;
      }
    }

    const last_path = path[path.length - 1];
    if (current_cave === "end") {
      collection.push(`${last_path}`);
    } else {
      graph[current_cave].forEach((cave) =>
        queue.push({ [cave]: `${last_path}` })
      );
    }
  }

  return collection.length;
};
// console.log(find_paths_bfs(graph, "start", []));

// PART 2
// to match two, I need to update my path checking condition to allow 2 instances for one small char
// create breadth first search
const find_paths_bfs_2 = (graph, start, path) => {
  const collection = [];

  const queue = [{ start: "", frequency_counter: {} }];

  while (queue.length > 0) {
    const temp = queue.shift();

    const current_cave = Object.keys(temp)[0];
    const current_path = Object.values(temp)[0];
    const current_small_caves = Object.values(temp)[1];

    if (current_cave === current_cave.toUpperCase()) {
      path.push(`${current_path},${current_cave}`);

      // if it is a small cave, check if it has been visited before
      // if not, add it to path
    } else {
      // do the updated check here
      //1. for this, filter the current path to remove big caves
      //2. count how many times each cave has been visited,
      //3. if there is not any small cave that has been visited twice, and current cave not in [start,end], we can visit the current_cave
      let count = current_small_caves[current_cave];
      current_small_caves[current_cave] = count ? count + 1 : 1;
      let num_visits = Object.values(current_small_caves);

      if (
        !num_visits.includes(2) ||
        !Object.keys(current_small_caves).includes(current_cave)
      ) {
        path.push(
          current_cave === "start"
            ? `${current_cave}`
            : `${current_path},${current_cave}`
        );

        // if it has been visited before, do not add it to path
      } else {
        const lastItem = path[path.length - 1];
        if (lastItem === lastItem.toLowerCase()) path.pop();
        continue;
      }
    }

    const last_path = path[path.length - 1];
    if (current_cave === "end") {
      collection.push(`${last_path}`);
    } else {
      graph[current_cave].forEach((cave) =>
        queue.push({
          [cave]: `${last_path}`,
          frequency_counter: current_small_caves,
        })
      );
    }
  }

  return collection.length;
};
console.log(find_paths_bfs_2(graph, "start", []));
