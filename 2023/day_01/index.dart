import 'dart:io';
import 'dart:convert';

isNumeric(string) => num.tryParse(string) != null;

Future readFileAsync(path) async {
  return await new File(path).readAsString();
}

void main() async {
  String input = await readFileAsync('./sample_input.txt');
  List inputList = input.split("\n");
  print(inputList);
  List numbers = [];

  for (var i = 0; i < input.length; i++) {
    List numbers = [];

    for (var j = 0; j < input[i].length; j++) {
        String curr = input[i][j];
        int val = int.parse(curr);
        if(val){
            numbers.add(val);
        }
    }

    print(numbers);
  }
}