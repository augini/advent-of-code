import 'dart:io';

bool isNumeric(String s) {
  if (s == null) {
    return false;
  }
  return double.tryParse(s) != null;
}

Future readFileAsync(path) async {
  return await new File(path).readAsString();
}

int partOne(List<String> input) {
  List<int> result = [];

  for (var i = 0; i < input.length; i++) {
    List<String> numbers = [];

    for (var j = 0; j < input[i].length; j++) {
      String curr = input[i][j];
      if (isNumeric(curr)) {
        numbers.add(curr);
      }
    }

    if (numbers.length > 0) {
      result.add(int.parse(numbers[0] + numbers.last));
    }
  }

  return result.reduce((a, b) => a + b);
}

// Steps - Part 2
// 1. Iterate over the input and append digits to the list
// 2. If the string starting from the current index starts with word representations of digits, append the index + 1 of that digit to the list
// 3. Create two digit numbers and return the sum

int partTwo(List<String> input) {
  List<int> result = [];
  const digitWords = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
  ];

  for (var i = 0; i < input.length; i++) {
    List<String> numbers = [];

    for (var j = 0; j < input[i].length; j++) {
      String curr = input[i][j];

      if (isNumeric(curr)) {
        numbers.add(curr);
      } else {
        for (var k = 0; k < digitWords.length; k++) {
          if (input[i].substring(j).startsWith(digitWords[k])) {
            numbers.add((k + 1).toString());
          }
        }
      }
    }

    if (numbers.length > 0) {
      result.add(int.parse(numbers[0] + numbers.last));
    }
  }

  return result.reduce((a, b) => a + b);
}

Future<void> main() async {
  String input = await readFileAsync('./input.txt');
  List<String> inputList = input.split("\n");

  // part 1
  print(partOne(inputList));

  // part 2
  print(partTwo(inputList));
}
