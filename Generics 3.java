//java program to demonstrate that NOT using
//generics can cause runtime exceptions

import java.util.*;

class Test
{
    public static void main(String[]args)
    {
    //creating an ArrayList without any type specified
    ArrayList al=new ArrayList<>();

    al.add("Sachin");
    al.add("Rahul");
    //al.add(10);//compiler allows this

//These lines would work just fine
    String s1=(String)al.get(0);
    String s2=(String)al.get(1);

    //NO runtime exception
    //String s3=(String)al.get(2);
    }
}
