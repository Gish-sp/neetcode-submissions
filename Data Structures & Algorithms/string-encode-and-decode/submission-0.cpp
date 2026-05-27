class Solution {
public:

    string encode(vector<string>& strs) {
        if (strs.empty()) return "";
        vector<int> sizes;
        string encoded_string;
        for (string& str: strs){
            sizes.push_back(str.size());
        }
        for (int sze: sizes){
            encoded_string += to_string(sze) + ';';
        }
        encoded_string += ':';
        for (string& st: strs){
            encoded_string += st;
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> decoded_strs;
        vector<int> sizes;
        if (s.empty()) return {};
        int i = 0;
        while (s[i] != ':'){
            string current_string = "";
            while(s[i] != ';'){
                current_string += s[i];
                i++;
            }
            sizes.push_back(stoi(current_string));
            i++;
        }
        i++;
        for (int sze: sizes){
            decoded_strs.push_back(s.substr(i,sze));
            i += sze;
        }
        return decoded_strs;
    }
};
