import os, datetime, time, random
import library.db_utils as db_utils
import app.sequence.service as sequence_service
import app.role.service as role_service
import app.endpoint.service as endpoint_service
import app.project.service as project_service
from bson.objectid import ObjectId

word_list = ["sed","ut","perspiciatis","unde","omnis","iste","natus","error","sit","voluptatem","accusantium","doloremque","laudantium","totam","rem","aperiam","eaque","ipsa","quae","ab","illo","inventore","veritatis","et","quasi","architecto","beatae","vitae","dicta","sunt","explicabo","nemo","enim","ipsam","quia","voluptas","aspernatur","aut","odit","fugit","consequuntur","magni","dolores","eos","qui","ratione","sequi","nesciunt","neque","porro","quisquam","est","dolorem","ipsum","dolor","amet","consectetur","adipisci","velit","non","numquam","eius","modi","tempora","incidunt","labore","dolore","magnam","aliquam","quaerat","ad","minima","veniam","quis","nostrum","exercitationem","ullam","corporis","suscipit","laboriosam","nisi","aliquid","ex","ea","commodi","consequatur","autem","vel","eum","iure","reprehenderit","in","voluptate","esse","quam","nihil","molestiae","illum","fugiat","quo","nulla","pariatur","at","vero","accusamus","iusto","odio","dignissimos","ducimus","blanditiis","praesentium","voluptatum","deleniti","atque","corrupti","quos","quas","molestias","excepturi","sint","occaecati","cupiditate","provident","similique","culpa","officia","deserunt","mollitia","animi","id","laborum","dolorum","fuga","harum","quidem","rerum","facilis","expedita","distinctio","nam","libero","tempore","cum","soluta","nobis","eligendi","optio","cumque","impedit","minus","quod","maxime","placeat","facere","possimus","assumenda","repellendus","temporibus","quibusdam","officiis","debitis","necessitatibus","saepe","eveniet","voluptates","repudiandae","recusandae","itaque","earum","hic","tenetur","a","sapiente","delectus","reiciendis","voluptatibus","maiores","alias","perferendis","doloribus","asperiores","repellat"]
word_list_length = len(word_list) - 1
char_list = list("abcdefghijklmnopqrstuvwxyz")
char_list_length = len(char_list) - 1
alphanum_list = list("abcdefghijklmnopqrstuvwxyz0123456789")
alphanum_list_length = len(alphanum_list) - 1
sentence_list = [
    "Nostrum doloremque eos sint pariatur quibusdam ducimus sint esse ut animi dolor",
    "Ipsum veritatis eveniet maxime veritatis quam rerum suscipit atque impedit optio voluptatum doloribus ut cumque ullam",
    "Fugiat modi accusamus libero ab voluptate sit at minus harum impedit maiores hic inventore aut",
    "Quibusdam occaecati quasi numquam sit sed aut odit enim quod magnam exercitationem ipsam ullam nulla illo facere",
    "Dolorem tenetur aliquid eaque aspernatur voluptas praesentium aliquid numquam quis",
    "Magni qui necessitatibus quae deserunt similique quas facilis voluptates debitis quod",
    "Alias cupiditate facere tempora maiores repudiandae accusamus soluta earum consequatur dolorem impedit beatae eius ratione aliquam expedita dolor",
    "Officiis nostrum perspiciatis impedit possimus occaecati fugiat pariatur aspernatur nesciunt magnam blanditiis cum consequuntur velit in minus numquam",
    "Aliquam nihil dolores facere aspernatur voluptates exercitationem repudiandae vel consectetur perferendis voluptas ipsum ipsa numquam placeat fugit illum",
    "Quisquam temporibus dolore nam blanditiis beatae consequuntur voluptatum recusandae quasi",
    "Nobis in debitis iusto reiciendis vero cumque atque tenetur magnam ex assumenda molestiae doloremque",
    "Perferendis tempore dolorem tenetur ex cupiditate hic dolorem occaecati vero nihil animi ut enim",
    "Eveniet perspiciatis voluptas quam consequatur alias mollitia ad porro soluta",
    "Occaecati officia esse sed pariatur deleniti explicabo ipsam consectetur veniam incidunt commodi quas vel optio blanditiis",
    "Ipsa quis cupiditate necessitatibus quasi dolores facilis minima iusto totam necessitatibus dolorum aspernatur qui a"
]
sentence_list_length = len(sentence_list) - 1

def traverse(structure, parent_reference, index):
    generated_data = {}
    for row in structure:
        if row["parentReference"] == parent_reference:
            if row['datatype'] == 'object':
                if row['array'] == True:
                    generated_data[row['name']] = [traverse(structure, row['reference'], i) for i in range(1, 5)]
                else:
                    generated_data[row['name']] = traverse(structure, row['reference'], index + 1)
            else:
                if row['array'] == True:
                    generated_data[row['name']] = [datagen(row['datatype'], row['lower'], row['upper'], i) for i in range(1, 5)]
                else:
                    generated_data[row['name']] = datagen(row['datatype'], row['lower'], row['upper'], index - 1)
    return generated_data

def datagen(datatype, lower, upper, index):
    if datatype == 'word':
        return " ".join([word_list[random.randint(0, word_list_length)] for i in range(0, random.randint(lower, upper))])
    elif datatype == 'sentence':
        return ". ".join([sentence_list[random.randint(0, sentence_list_length)] for i in range(0, random.randint(lower, upper))])
    elif datatype == 'char':
        return "".join([char_list[random.randint(0, char_list_length)] for i in range(0, random.randint(lower, upper))])
    elif datatype == 'integer':
        return random.randint(lower, upper)
    elif datatype == 'decimal':
        return random.uniform(lower, upper)
    elif datatype == 'alphanumeric':
        return "".join([alphanum_list[random.randint(0, alphanum_list_length)] for i in range(0, random.randint(lower, upper))])
    elif datatype == 'sequence_number':
        return lower + index
    elif datatype == 'boolean':
        return bool(random.getrandbits(1))
    elif datatype == 'enum':
        return ''
    else:
        return "unsupported data type"


