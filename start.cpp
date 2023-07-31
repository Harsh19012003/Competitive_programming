#include <bits/stdc++.h>
#include <array>
#include <vector>

using namespace std;


class Student{
    public:
        string name;
        int roll_no;
        string surname;
    
        // constructor overloading
        Student(){
            name = "";
            roll_no = -1;
            surname = "";
        }

        Student(string arg1, int arg2, string arg3){
            name = arg1;
            roll_no = arg2;
            surname = arg3;
        }

        // Methods
        string full_name(){
            return name+surname;
        }
};


class Engineering_student : public Student{
    public:
    int package;

    Engineering_student(){
        package = 0;
    }
    Engineering_student(int argp){
        package = argp;
    }
};


float rand_num(string xyz, int num){
    cout << xyz << endl;
    num++;
    return num;
}

void by_reference(int &x){
    x++;
    return;
}



int main(){
    // or fast input output
    ios::sync_with_stdio(0);
    cin.tie(0);


    // PRINTING TO CONSOLE
    string name = "john";
    int age;
    age = 20;
    cout << "name is" << name << " he is old:" << age << endl;


    // DATATYPES IN C++
    char character = 'x';
    string strg = "xyz";
    int integer = 5;
    float decimal = -10.11;
    double big_decimal = 12.2345;
    bool boolean_var = true;
    cout << character << strg << integer << decimal << big_decimal << boolean_var << false << endl;


    // STRINGS METHODS
    string str = "Lets say this is the string";
    cout << str.find("is", 2) << endl; // find arg1 start searching from arg2
    cout << str.substr(5, 3) << endl;


    // BASIC MATH
    double a = 50.0, b = 6.0;
    cout << a/b << endl;


    // INPUT
    char trial;
    cout << "Enter age: ";
    // cin >> trial; 
    cout << trial << endl;
    string s;
    cout << "again via getline: ";
    // getline(std::cin, s);
    cout << "whole line getline" << s << endl;
    

    // ARRAYS
    int arr[10];
    arr[5] = 5;
    cout << arr[5] << endl;
    cout << arr[1] << "Garbage val" << endl;


    // FUNCTION
    cout << rand_num("hehe", 4) << endl;
    int pass_by_reference = 0;
    by_reference(pass_by_reference);
    cout << "pbr result  " << pass_by_reference << "\n";


    // if (condition){
    //     do this;
    // }
    // elif(other condition){
    // }
    // else{
    // }

    // switch(expression){
    // case 1:
    //     do this;
    //     break;
    // case 2:
    //     so this;
    // case 3:
    //     and this;
    // default:
    //     atlast this;
    // }

    // while(expression){
    //     do this;
    // }
    // do{
    //     this;
    // }
    // while(expression)

    // for(int i = 0; i < something; i++){
    //     do this;
    // }

    string asdf = "Harshkumar Devmurari";
    for (char c : asdf){
        cout << c << " ";
    }
    cout << "\n";


    // POINTERS
    int number = 5;
    int *pnumber = &number;
    cout << number << "\t" << pnumber << "\t" << *pnumber << "\t" << &*pnumber << "\t" << &number << endl;


    // OOPS
    Student student1("aashish", 2, "chaudhari");
    Student student2("harsh", 11, "devmurari");
    cout << "full name is: " << student2.full_name() << endl;
    cout << student2.roll_no << endl;

    Student student3;
    cout << student3.name << endl;
    cout << student3.roll_no << endl;

    Engineering_student student5(12000000);
    student5.name = "Yash";
    cout << student5.full_name() << student5.package << endl;


    // ARRAYS ARE BY DEFAULT PASSED ON TO FUCTIONS AS A POINTER i.e PASSED BY REFERENCE
    // ARRAYS: 2 types:
    // 1) built in array: int array[3] = {10, 20, 30};
    // 2) array library: #include <array>   array<int, 3> name_of_the_array {10, 20, 30};       have inbuilt methods like array.size()
    array<int, 3> array_lib {1,2,3};
    cout <<"size of array_lib is: " << array_lib.size() << "\n";

    // for (int i = 0; array_lib.size()-1; i++){
    //         for (int j = 0; j < array_lib.size()-1; j++){
    //             if (i!=j){
    //                 if (array_lib[i] == array_lib[j]){
    //                     cout << "true";
    //                 }
    //             }
                
    //         }
    //     }
    // cout << "false";


    // VECTORS
    vector<int> vec;
    // vec[0] = 1;
    // cout << vec[0] << endl;
    vec = {10, 20, 30, 40, 50};
    for (int i = 0; i < vec.size(); i++){
        cout << vec[i] << "\t";
    }
    
    return 0;
}