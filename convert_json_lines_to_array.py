import json

def convert_json_lines_to_array(input_file_path, output_file_path):
    """
    JSON Lines 형식의 파일을 읽어 JSON 배열 형식의 파일로 변환합니다.

    Args:
        input_file_path (str): 원본 JSON Lines 파일 경로
        output_file_path (str): 변환된 JSON 배열 파일 경로
    """
    # 원본 JSON 파일을 읽어서 리스트로 변환
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    # 각 줄을 JSON 객체로 변환하고 리스트에 추가
    json_list = []
    for line in lines:
        try:
            json_obj = json.loads(line.strip())
            json_list.append(json_obj)
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e} for line: {line}")

    # 변환된 JSON 리스트를 JSON 배열 형식으로 저장
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(json_list, outfile, ensure_ascii=False, indent=4)

    print(f"JSON array file saved to {output_file_path}")

input_file_path = './Dataset/MedMCQA/dev.txt'
output_file_path = './Dataset/MedMCQA/dev.json'
convert_json_lines_to_array(input_file_path, output_file_path)
input_file_path = './Dataset/MedMCQA/train.txt'
output_file_path = './Dataset/MedMCQA/train.json'
convert_json_lines_to_array(input_file_path, output_file_path)
