import 'package:flutter/material.dart';
import 'package:fetch_data_demo/pages/home.dart';
import 'package:fetch_data_demo/pages/Stress.dart';
import 'package:fetch_data_demo/pages/query_data.dart';
import 'package:fetch_data_demo/pages/save_data.dart';

// This is a demo page to show StatefulWidgets
class NavigatePage extends StatefulWidget {
  const NavigatePage({super.key});

  @override
  State<NavigatePage> createState() => _NavigatePageState();
}

// This function update login page given state change
class _NavigatePageState extends State<NavigatePage> {
  // used to show selected icon
  int _selectedIndex = 0;

  // update index as pressing icon
  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  final  List<Widget> _screen = <Widget>[
      HomePage(),
      QueryData(),
      SaveData(),
      StressPage(),
    ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            label: "Home",
            icon: Icon(Icons.home, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "Search",
            icon: Icon(Icons.cloud_circle, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "Stress",
            icon: Icon(Icons.rate_review, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "Reference",
            icon: Icon(Icons.balance, color: Colors.green),
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.amber[800],
        onTap: _onItemTapped,
      ),
      body: _screen.elementAt(_selectedIndex),
    ); 
  }
}