using namespace std; 
  
// Function to print the string 
void printString(string str, char ch, int count) 
{ 
    int occ = 0, i; 
  
    // If given count is 0 
    // print the given string and return 
    if (count == 0) { 
        cout << str; 
        return; 
    } 
  
    // Start traversing the string 
    for (i = 0; i < str.length(); i++) { 
  
        // Increment occ if current char is equal 
        // to given character 
        if (str[i] == ch) 
            occ++; 
  
        // Break the loop if given character has 
        // been occurred given no. of times 
        if (occ == count) 
            break; 
    } 
  
    // Print the string after the occurrence 
    // of given character given no. of times 
    if (i < str.length() - 1) 
        cout << str.substr(i + 1, str.length() - (i + 1)); 
  
    // Otherwise string is empty 
    else
        cout << "Empty string"; 
} 
  
// Drivers code 
int main() 
{ 
    string str = "geeks for geeks"; 
    printString(str, 'e', 2); 
    return 0; 
} 
