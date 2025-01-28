//refernce: https://www.geeksforgeeks.org/flutter-working-with-layouts/

import 'package:flutter/material.dart';

// This is a demo page to show layout widgets
class DemoLayoutWidgets extends StatefulWidget {
  const DemoLayoutWidgets({super.key});

  @override
  State<DemoLayoutWidgets> createState() => _DemoLayoutUpdateState();
}

// This function update page given state change
class _DemoLayoutUpdateState extends State<DemoLayoutWidgets> {
  // used to show selected icon
  int _selectedIndex = 0;

  // update index as pressing icon
  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  final  List<Widget> _screen = <Widget>[
      _buildContainer(),
      _buildImageRow(),
      _buildImageColumn(),
      _buildGrid(),
      _buildList(),
    ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Layout Demo'),
      ),
      // body: Center(
      //   // replace this section in your app to test different layout
      //   child: _buildContainer(),
      //   // child: _buildImageRow(),
      //   // child: _buildImageColumn(),
      //   // child: _buildGrid(),
      //   // child: _buildList(),
      // )
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            label: "Container",
            icon: Icon(Icons.home, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "ImageRow",
            icon: Icon(Icons.cloud_circle, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "ImageColumn",
            icon: Icon(Icons.access_alarm, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "Grid",
            icon: Icon(Icons.rate_review, color: Colors.green),
          ),
          BottomNavigationBarItem(
            label: "List",
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

Widget _buildContainer() => Container(
    // Container implementation
    child: Container(
      height: 100.0,
      width: 100.0,
      color: const Color.fromARGB(255, 76, 127, 175),
    )
);

// function returning column widget
Widget _buildImageColumn() => Container(
  decoration: BoxDecoration(
    color: Colors.black12,
  ),
  child: Column(
    children: [
      Container(
        height: 100.0,
        width: 50.0,
        color: Colors.red,
      ),
      Container(
        height: 100.0,
        width: 50.0,
        color: Colors.yellow,
      ),
    ],
  ),
);

// function returning column widget
Widget _buildImageRow() => Container(
  decoration: BoxDecoration(
    color: Colors.black12,
  ),
  child: Row(
    children: [
      Container(
        height: 50.0,
        width: 80.0,
        color: Colors.red,
      ),
      Container(
        height: 50.0,
        width: 80.0,
        color: Colors.yellow,
      ),
    ],
  ),
);


// Method returning Grid Widget
Widget _buildGrid() => GridView.extent(
  maxCrossAxisExtent: 150,
  padding: const EdgeInsets.all(4),
  mainAxisSpacing: 4,
  crossAxisSpacing: 4,
  children: _buildGridTileList(10));
 
List<Container> _buildGridTileList(int count) => List.generate(
  count,
  (i) => Container(
        width: 100,
        height: 100,
        color: Colors.blue,
      ));

// function returning List view widget
Widget _buildList() => ListView(
   
        // name is a listTile widget which is defined below
      children: [
        name('james', 'thomas'), 
        name('Ajay', 'kumar'),
        name('Arun', 'das'),
        name('Roxie', 'St'),
        name('Stanlee', 'jr'),
        name('AMC', 'hales'),
        Divider(),
        name('Monty',"Chopra"),
        name('Emmy', 'Ave'),
        name(
            'Chaitanya', ' kumar'),
        name('Rio', 'St'),
      ],
    );
 
// name is a function returning ListTile widget
ListTile name(String firstName, String lastName) => ListTile(
      title: Text(firstName,
          style: TextStyle(
            fontWeight: FontWeight.w500,
            fontSize: 20,
          )),
      subtitle: Text(lastName),
      leading: Icon(
        Icons.arrow_back_ios,
        color: Colors.blue[500],
      ),
    );