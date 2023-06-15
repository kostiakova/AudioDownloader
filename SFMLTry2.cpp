#include <SFML/Graphics.hpp>
#include <SFML/Window/Event.hpp>
#include <SFML/Window/Cursor.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <iostream>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <SFML/Main.hpp>
#include <direct.h>
#include <fstream>
#include <format>
#include <Windows.h>

using namespace sf;
using namespace std;

string getdir() {
    string cur_dir;
    cur_dir = _getcwd(0, 0);
    cout << cur_dir<<endl;
    const char* full_dir = cur_dir.c_str();
    int check = _mkdir(full_dir);
        
    if (!check)
        printf("Directory created\n");
    else {
        printf("Unable to create directory\n");
    }
    return cur_dir;
}

string working_files(string dir) {
    ifstream file(dir + "\\res\\last.txt");
    string title, temp;
    if (file.is_open()) {
        while (file.good()) {
            file >> temp;
            temp += " ";
            title += temp;
        }
    }
    //cout << title<<endl;
    return title;
}

void writing_files(string link, string dir) {
    ofstream file(dir + "\\res\\last.txt");
    file << link;
}

int main() {
    setlocale(LC_ALL, "Russian");
    string command_call = "engine.exe --only_title";
    const int MAXCHARACTERSNUM = 25;
    string voidd = "";
    string endline = "\n";
    system("engine.exe");
    string dir = getdir();


    RenderWindow window(VideoMode(1024, 768), "Audio Downloader");



    CircleShape shape(308.5f);
    shape.setFillColor(Color::Green);


    RectangleShape InputRect(Vector2f(610, 60));
    InputRect.setFillColor(Color::Magenta);
    InputRect.move(Vector2f(205, 30));




    RectangleShape ButtonRectangle(Vector2f(150, 100));
    ButtonRectangle.setFillColor(Color::Magenta);
    ButtonRectangle.move(Vector2f(437, 434));

    Font font1;
    font1.loadFromFile(dir + "\\arial.ttf");





#pragma region text1
    Text text1;
    text1.setString(L"Text1++");
    text1.setFont(font1);
    text1.setCharacterSize(50);
    text1.setFillColor(Color::Cyan);
    text1.move(Vector2f(500, 200));
#pragma endregion text1



#pragma region VideoTitle
    String videoTitle;
    Text Video_Title;
    Video_Title.setFont(font1);
    Video_Title.setCharacterSize(50);
#pragma endregion VideoTitle



#pragma region Button
    bool mouseOverButton = false;
#pragma endregion Button


#pragma region TextEntry
    bool selectedEntry, hoverEntry = false;
    string Link;
    Text LinkEntry;
    LinkEntry.setString("TextEtry");
    LinkEntry.setFont(font1);
    LinkEntry.setCharacterSize(50);
    LinkEntry.setPosition(205, 30);
    LinkEntry.setFillColor(Color::Black);
#pragma endregion TextEntry




    while (window.isOpen())
    {
        Event event;
        while (window.isOpen())
        {
            Event event;
            while (window.pollEvent(event)) {
                switch (event.type)
                {
                case Event::TextEntered:
                    if (selectedEntry) {
                        if (event.text.unicode == 8) { //backspace 
                            if (!Link.empty()) {
                                Link.pop_back();
                            }
                        }
                        else if (event.text.unicode == 22) { // Ctrl+V
                            try
                            {
                                Link = Clipboard::getString();
                            }
                            catch (const std::exception&)
                            {
                                cout << "Error! " << endl;
                            }

                            if (Link.size() >= 25 && Link[25] != voidd) {
                                Link.insert(25, endline.c_str());
                                LinkEntry.setCharacterSize(25);

                                if (Link.size() >= 49 && Link[49] != voidd) {
                                    Link.insert(49, endline.c_str());
                                    LinkEntry.setCharacterSize(16);

                                    if (Link.size() >= 74 && Link[74] != voidd) {
                                        Link.insert(74, endline.c_str());
                                        LinkEntry.setCharacterSize(10);
                                    }
                                }
                            }
                        }
                        else if (event.text.unicode < 128) { // Text
                            Link += event.text.unicode;

                            std::string wrappedString;
                            int currentPosition = 0;
                            for (sf::Uint32 ch : Link) {
                                wrappedString += static_cast<char>(ch);
                                currentPosition++;

                                if (currentPosition == MAXCHARACTERSNUM) {
                                    wrappedString += '\n';
                                    currentPosition = 0;
                                    Link = wrappedString;
                                }
                            }

                        }

                            else { LinkEntry.setCharacterSize(50); }
                            LinkEntry.setString(Link);


                        }
                    
                    break;


                case Event::Closed:
                    window.close();
                    break;
                case Event::MouseButtonPressed:
                    if (mouseOverButton) {
                        writing_files(Link, dir);
                        cout << "Button pressed: "  << " " << endl;
                        system("engine.exe");
                    }
                    else if (hoverEntry) {
                        selectedEntry = true;
                        cout << "Pressed" <<endl;
                    }
                    else if (!selectedEntry) {
                        writing_files(Link, dir); 
                        system(command_call.c_str());
                        Sleep(1500);
                        string title = working_files(dir);
                        text1.setString(title);
                    }
                    break;
                }

            }




            if (Mouse::getPosition(window).x >= ButtonRectangle.getPosition().x && Mouse::getPosition(window).x <= ButtonRectangle.getPosition().x + 150 &&
                Mouse::getPosition(window).y >= ButtonRectangle.getPosition().y && Mouse::getPosition(window).y <= ButtonRectangle.getPosition().y + 100) {
                ButtonRectangle.setFillColor(Color(23, 200, 124));
                mouseOverButton = true;
            }
            else if (Mouse::getPosition(window).x >= LinkEntry.getPosition().x && Mouse::getPosition(window).x <= LinkEntry.getPosition().x + 150 &&
                Mouse::getPosition(window).y >= LinkEntry.getPosition().y && Mouse::getPosition(window).y <= LinkEntry.getPosition().y + 100) {
                hoverEntry = true;
            }


            else { ButtonRectangle.setFillColor(Color::Magenta); mouseOverButton = false; hoverEntry = false; selectedEntry = false; }
            window.clear(Color::White);
            window.draw(InputRect);
            window.draw(text1);
            window.draw(ButtonRectangle);
            window.draw(LinkEntry);
            window.display();
        }
    }
}