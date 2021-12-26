const flash_octopuses = (coords) => {
  const new_coords = coords.split("\n");

  for (let i = 0; i < new_coords.length; i++) {
    new_coords[i] = new_coords[i].split("");
    for (let y = 0; y < new_coords[i].length; y++) {
      new_coords[i][y] = parseInt(new_coords[i][y]);
    }
  }

  // start BFS traversing the grid
  // queue is a list of coordinates seperated by commas
  let flashes = 0;

  for (let step = 0; step < 100; step++) {
    // set/object to store the flashed coordinates in this step
    let flashed = [];

    for (let x = 0; x < new_coords.length; x++) {
      for (let y = 0; y < new_coords[x].length; y++) {
        if (new_coords[x][y] < 9 && !flashed.includes(`${x},${y}`)) {
          new_coords[x][y] += 1;
        } else if (new_coords[x][y] === 9) {
          const queue = [`${x},${y}`];

          while (queue.length > 0) {
            const current = queue.shift();

            // get current coordinates
            let [x, y] = current.split(",");
            x = parseInt(x);
            y = parseInt(y);

            // flash the element if it equals 9 and push its neighbors to queue
            if (new_coords[x][y] === 9) {
              new_coords[x][y] = 0;
              flashes += 1;

              // add the currently visited index to flashed
              // so that we do not flash it again in the current step
              flashed.push(`${x},${y}`);

              // add the neighbors to the queue
              let neighbors = [];
              // top row
              if (new_coords[x - 1]?.[y - 1] !== undefined)
                neighbors.push(`${x - 1},${y - 1}`);

              if (new_coords[x - 1]?.[y] !== undefined)
                neighbors.push(`${x - 1},${y}`);

              if (new_coords[x - 1]?.[y + 1] !== undefined)
                neighbors.push(`${x - 1},${y + 1}`);

              // bottom row
              if (new_coords[x + 1]?.[y - 1] !== undefined)
                neighbors.push(`${x + 1},${y - 1}`);

              if (new_coords[x + 1]?.[y] !== undefined)
                neighbors.push(`${x + 1},${y}`);

              if (new_coords[x + 1]?.[y + 1] !== undefined)
                neighbors.push(`${x + 1},${y + 1}`);

              // same row
              if (new_coords[x]?.[y - 1] !== undefined)
                neighbors.push(`${x},${y - 1}`);
              if (new_coords[x]?.[y + 1] !== undefined)
                neighbors.push(`${x},${y + 1}`);

              queue.push(...neighbors);

              neighbors = [];
            } else if (!flashed.includes(`${x},${y}`)) {
              // otherwise, increment the value by one
              new_coords[x][y] += 1;
            }
          }
        }
      }
    }
    flashed = [];
  }

  return flashes;
};

// console.log(
//   flash_octopuses(`8271653836
// 7567626775
// 2315713316
// 6542655315
// 2453637333
// 1247264328
// 2325146614
// 2115843171
// 6182376282
// 2384738675`)
// );

const flash_octopuses_simultaneously = (coords) => {
  const new_coords = coords.split("\n");

  for (let i = 0; i < new_coords.length; i++) {
    new_coords[i] = new_coords[i].split("");
    for (let y = 0; y < new_coords[i].length; y++) {
      new_coords[i][y] = parseInt(new_coords[i][y]);
    }
  }

  // start BFS traversing the grid
  // queue is a list of coordinates seperated by commas
  let flashes = 0;
  let final_step = 0;

  for (let step = 0; step < 500; step++) {
    // set/object to store the flashed coordinates in this step
    let flashed = [];

    for (let x = 0; x < new_coords.length; x++) {
      for (let y = 0; y < new_coords[x].length; y++) {
        if (new_coords[x][y] < 9 && !flashed.includes(`${x},${y}`)) {
          new_coords[x][y] += 1;
        } else if (new_coords[x][y] === 9) {
          const queue = [`${x},${y}`];
          visited = {};

          while (queue.length > 0) {
            const current = queue.shift();
            // get current coordinates
            let [x, y] = current.split(",");
            x = parseInt(x);
            y = parseInt(y);

            // flash the element if it equals 9 and push its neighbors to queue
            if (new_coords[x][y] === 9) {
              new_coords[x][y] = 0;
              flashes += 1;

              // add the currently visited index to flashed
              // so that we do not flash it again in the current step
              flashed.push(`${x},${y}`);

              // add the neighbors to the queue
              let neighbors = [];
              // top row
              if (new_coords[x - 1]?.[y - 1] !== undefined)
                neighbors.push(`${x - 1},${y - 1}`);

              if (new_coords[x - 1]?.[y] !== undefined)
                neighbors.push(`${x - 1},${y}`);

              if (new_coords[x - 1]?.[y + 1] !== undefined)
                neighbors.push(`${x - 1},${y + 1}`);

              // bottom row
              if (new_coords[x + 1]?.[y - 1] !== undefined)
                neighbors.push(`${x + 1},${y - 1}`);

              if (new_coords[x + 1]?.[y] !== undefined)
                neighbors.push(`${x + 1},${y}`);

              if (new_coords[x + 1]?.[y + 1] !== undefined)
                neighbors.push(`${x + 1},${y + 1}`);

              // same row
              if (new_coords[x]?.[y - 1] !== undefined)
                neighbors.push(`${x},${y - 1}`);
              if (new_coords[x]?.[y + 1] !== undefined)
                neighbors.push(`${x},${y + 1}`);

              queue.push(...neighbors);

              neighbors = [];
            } else if (!flashed.includes(`${x},${y}`)) {
              // otherwise, increment the value by one
              new_coords[x][y] += 1;
            }
          }
        }
      }
    }

    // check if all the elements are same
    let all_same = true;
    for (let line = 0; line < new_coords.length; line++) {
      let temp = new_coords[line].every(
        (element) => element === new_coords[0][0]
      );

      if (!temp) all_same = false;
    }

    flashed = [];

    if (all_same) {
      final_step = step;
      break;
    }
  }

  return final_step + 1;
};

console.log(
  flash_octopuses_simultaneously(`8271653836
7567626775
2315713316
6542655315
2453637333
1247264328
2325146614
2115843171
6182376282
2384738675`)
);
