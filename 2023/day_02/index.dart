import 'dart:io';

Future readFileAsync(path) async {
  return await new File(path).readAsString();
}

int partOne(List<String> input) {
  // Solve part 1
  return 1;
}

int partTwo(List<String> input) {
  // Solve part 2

  return 2;
}

Future<void> main(List<String> args) async {
  String input = await readFileAsync(args[0]);
  List<String> inputList = input.split("\n");

  // part 1
  print(partOne(inputList));

  // part 2
  print(partTwo(inputList));
}
