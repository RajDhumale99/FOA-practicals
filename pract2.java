 /*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.test11;

import java.awt.BorderLayout;
import java.awt.Container;
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;


public class pract2 extends JFrame implements ListSelectionListener
{
JLabel jl1;
	
JList list;
	
JTextField jtf;
	
String name[]={"A","B","C","D","E"};

public pract2()
{
    Container cp=getContentPane();
		
cp.setLayout(new BorderLayout());
		
jl1=new JLabel("Select a BOOK");
		
cp.add(jl1,BorderLayout.NORTH);
		
list=new JList(name);
		
list.addListSelectionListener(this);
		
cp.add(list,BorderLayout.CENTER);
		
jtf=new JTextField(15);
		
cp.add(jtf,BorderLayout.SOUTH);
	
}
	
		
public void valueChanged(ListSelectionEvent le)
		
{
			
int i=list.getSelectedIndex();
			
if(i==0)
			
{
				
jtf.setText("Book A is Selected....");
			
}
			
else if(i==1)
			
{
				
jtf.setText("Book B is Selected....");
			
}
			
else if(i==2)
			
{
				
jtf.setText("Book C is Selected....");
			
}
			
else if(i==3)
			
{
				
jtf.setText("Book D is Selected....");
			
}
			
else if(i==4)
			
{
				
jtf.setText("Book E is Selected....");
			
}
			
else
			
{
				
jtf.setText("Select Book......");
			
}

}
    public static void main(String[] args) 
    {
     pract2 p1=new pract2();
		
p1.setSize(500,500);
		
p1.setVisible(true);
		
p1.setTitle("Library Mng. System");
		
p1.setDefaultCloseOperation(EXIT_ON_CLOSE);
	
}
}
