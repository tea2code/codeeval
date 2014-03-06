#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief Solves the Even Numbers challenge.
 * See https://www.codeeval.com/open_challenges/100/
 */
class EvenNumbers
{
public:
    /**
     * @brief Check every number if even.
     * @param numbers
     * @return List of boolean indicating if number at index is even.
     */
    vector<bool> areAllEven(const vector<int>& numbers)
    {
        vector<bool> result;
        for(const int& number : numbers)
        {
            result.push_back(isEven(number));
        }
        return result;
    }

    /**
     * @brief Check if a number is even.
     * @param number
     * @return True if number is even else false.
     */
    bool isEven(int number)
    {
        return number % 2 == 0;
    }

    /**
     * @brief Read input file.
     * @param fileName
     * @return List of numbers.
     */
    vector<int> readInput(const string& fileName)
    {
        vector<int> result;

        ifstream file(fileName.c_str());
        string line;
        while (!file.eof())
        {
            getline(file, line);
            if (line.length() == 0)
            {
                continue;
            }
            result.push_back(atoi(line.c_str()));
        }

        return result;
    }
};

int main(int argc, const char* argv[])
{
    if (argc != 2)
    {
        return 1;
    }
    EvenNumbers en;
    vector<int> numbers = en.readInput(argv[1]);
    vector<bool> results = en.areAllEven(numbers);
    for(bool result : results)
    {
        cout << result << endl;
    }
    return 0;
}
