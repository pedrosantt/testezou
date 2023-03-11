import 'dart:io';

void main() {
  var lista = [];
  for (int i = 0; i < 10; i++) {
    print('digite um numero');
    int? input = int.parse(stdin.readLineSync()!);
    lista.add(input);
  }
  lista.sort();
  lista.remove(0);
  lista.remove(1);
  lista.remove(2);
  lista.clear();
  print(lista);
}
