import 'dart:io';
import 'dart:convert';

bool isNumeric(String s) {
  if (s == null) {
    return false;
  }
  return double.tryParse(s) != null;
}

Future readFileAsync(path) async {
  return await new File(path).readAsString();
}

Future<void> main() async {
  String input = await readFileAsync('./input.txt');
  List<String> inputList = input.split("\n");
  List<int> result = [];

  // part 1
  for (var i = 0; i < inputList.length; i++) {
    List<String> numbers = [];
    for (var j = 0; j < inputList[i].length; j++) {
      String curr = inputList[i][j];
      if (isNumeric(curr)) {
        numbers.add(curr);
      }
    }
    if (numbers.length > 0) {
      result.add(int.parse(numbers[0] + numbers.last));
    }
  }

  // print(result.reduce((a, b) => a + b));

  // part 2

  result = [];
  const matches = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
  ];

  Map<String, String> wordToDigitMap = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
  };

  for (var i = 0; i < inputList.length; i++) {
    String currentLine = inputList[i];
    int min = currentLine.length;
    String charAtMin = '';

    int max = 0;
    String charAtMax = '';

    for (var j = 0; j < matches.length; j++) {
      // Find the first occurrence of the search term
      String searchTerm = matches[j];

      int firstOccurrenceIndex = currentLine.indexOf(searchTerm);

      if (firstOccurrenceIndex != -1) {
        if (firstOccurrenceIndex < min) {
          min = firstOccurrenceIndex;
          charAtMin = searchTerm;
        }
      }

      // Find the last occurrence of the search term
      int lastOccurrenceIndex = currentLine.lastIndexOf(searchTerm);
      if (lastOccurrenceIndex != -1) {
        if (lastOccurrenceIndex > max) {
          max = lastOccurrenceIndex;
          charAtMax = searchTerm;
        }
      }
    }

    String? digitOne = charAtMin;
    String? digitTwo = charAtMax;

    if (wordToDigitMap.containsKey(charAtMin)) {
      digitOne = wordToDigitMap[charAtMin];
    }

    if (wordToDigitMap.containsKey(charAtMax)) {
      digitTwo = wordToDigitMap[charAtMax];
    }

    print('$digitOne$digitTwo');
    if('$digitOne$digitTwo'.length > 1){
      result.add(int.parse('$digitOne$digitTwo'));
    }
  }
  print(result.reduce((a, b) => a + b));
}
