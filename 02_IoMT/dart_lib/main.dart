import 'package:flutter/material.dart';
import 'package:demo_code/pages/login.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // This line remove debug banner on the screen
      debugShowCheckedModeBanner: false,
      // home: const DemoStatefulWidgets(),
      // home: const DemoStatelessWidgets(),
      home: LoginPage(),
    );
  }
}


