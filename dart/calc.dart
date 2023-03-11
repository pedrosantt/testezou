import 'dart:io';

void main() {
  print('digite um numero');
  int? input = int.parse(stdin.readLineSync()!);
  double A = 3.14 * input * input;
  print(A);
}
