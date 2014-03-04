#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

/**
 * @brief Solves the Penultimate Word challenge.
 * See https://www.codeeval.com/open_challenges/92/
 */
class PenultimateWord
{
public:
    /**
     * @brief Read input file.
     * @param fileName
     * @return List of lines.
     */
    std::vector<std::string> readInput(const std::string& fileName)
    {
        std::vector<std::string> result;

        std::ifstream file(fileName.c_str());
        std::string line;
        while (!file.eof())
        {
            std::getline(file, line);
            if (line.length() == 0)
            {
                continue;
            }
            result.push_back(line);
        }

        return result;
    }

    /**
     * @brief Find the next to last word for every given line.
     * @param lines
     * @return List of words.
     */
    std::vector<std::string> nextToLast(std::vector<std::string> lines)
    {
        std::vector<std::string> result;
        for(std::vector<std::string>::iterator it = lines.begin(); it != lines.end(); ++it)
        {
            std::string nextToLast = *(split(*it, ' ').rbegin() + 1);
            result.push_back(nextToLast);
        }
        return result;
    }

private:
    /**
     * @brief Split a string using given delimiter.
     * @param str
     * @param delimiter
     * @return The splitted string.
     */
    std::vector<std::string> split(const std::string& str, char delimiter)
    {
        std::istringstream is(str);
        std::vector<std::string> result;
        for(std::string cur; std::getline(is, cur, delimiter); result.push_back(cur));
        return result;
    }
};

int main(int argc, const char* argv[])
{    
    if (argc != 2)
    {
        return 1;
    }
    PenultimateWord pw;
    std::vector<std::string> lines = pw.readInput(argv[1]);
    std::vector<std::string> nextToLasts = pw.nextToLast(lines);
    for(std::vector<std::string>::iterator it = nextToLasts.begin(); it != nextToLasts.end(); ++it)
    {
        std::cout << *it << std::endl;
    }
    return 0;
}

