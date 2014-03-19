#include <cmath>
#include <fstream>
#include <iostream>
#include <regex>
#include <string>
#include <utility>
#include <vector>

/**
 * @brief Solves the Calculate Distance challenge.
 * See https://www.codeeval.com/open_challenges/99/
 */
class CalculateDistance
{
public:
    /**
     * @brief A single point in 2D.
     */
    struct Point
    {
        int x;
        int y;
    };

    using PointPair = std::pair<Point, Point>;

    /**
     * @brief Read input file.
     * @param fileName
     * @return List of lines.
     */
    std::vector<PointPair> readInput(const std::string& fileName)
    {
        std::vector<PointPair> result;

        std::regex rx(R"(\(\s*([\d-]+)\s*,\s*([\d-]+)\s*\)\s*\(\s*([\d-]+)\s*,\s*([\d-]+)\s*\))");
        std::cmatch match;

        std::ifstream file(fileName.c_str());
        std::string line;
        while (!file.eof())
        {
            std::getline(file, line);
            if (line.length() == 0)
            {
                continue;
            }

            std::regex_search(line.c_str(), match, rx);
            Point a {std::atoi(match[0].str().c_str()), std::atoi(match[1].str().c_str())};
            Point b {std::atoi(match[2].str().c_str()), std::atoi(match[3].str().c_str())};
            PointPair pair {a, b};

            result.push_back(pair);
        }

        return result;
    }

    /**
     * @brief Calculate euclidian distance of two points.
     * @param a First point.
     * @param b Second point.
     * @return The distance as an integer.
     */
    int distance(Point a, Point b)
    {
        int result = std::sqrt(std::pow(a.x - b.x, 2) + std::pow(a.y - b.y, 2));
        return result;
    }
};

int main(int argc, const char* argv[])
{    
    if (argc != 2)
    {
        return 1;
    }
    CalculateDistance cd;
    std::vector<CalculateDistance::PointPair> points = cd.readInput(argv[1]);
    for(auto& pair : points)
    {
        std::cout << cd.distance(pair.first, pair.second) << std::endl;
    }
    return 0;
}

