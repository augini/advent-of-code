import 'dart:io';

Future readFileAsync(path) async {
  return await new File(path).readAsString();
}

bool isNumeric(String s) {
  return double.tryParse(s) != null;
}

int partOne(List<String> data) {
  // Solve part 1
  Map<String, int> valid = {"red": 12, "green": 13, "blue": 14};
  Set<int> invalid = {};

  data.forEach((item) {
    List<String> pieces = item.split(":");
    List<String> games = pieces[1].split(";");

    games.forEach((element) {
      List<String> matches = element.split(" ");
      Map<String, int> records = {"red": 0, "green": 0, "blue": 0};

      matches.forEach((match) {
        if (isNumeric(match)) {
          int number = matches.indexOf(match);
          String color = matches[number + 1].replaceFirst(",", "");

          records[color] = records[color]! + number;
          for (int i = 0; i < valid.length; i++) {}
        }
      });
    });
  });

  // for item in data:
  //     pieces = item.split(":")
  //     id = pieces[0].split(" ")[1]
  //     games = pieces[1].split(";")

  //     for each in games:
  //         matches = each.split(" ")
  //         records = {"red": 0, "green": 0, "blue": 0}
  //         for index, number in enumerate(matches):
  //             if number.isdigit():
  //                 color = matches[index + 1].replace(",", "")
  //                 records[color] += int(number)

  //         for values in zip(valid.values(), records.values()):
  //             if values[0] < values[1]:
  //                 invalid.add(int(id))
  //                 break

  // return sum(range(1, len(data) + 1)) - sum(invalid)

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
