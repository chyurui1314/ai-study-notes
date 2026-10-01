#1. **新增岗位**：输入岗位名称、招聘单位、工作地点、薪资范围、备注，保存到岗位列表
#2. **按名称查询岗位**：输入岗位关键词，找到后显示该岗位全部信息
#3. **修改岗位薪资**：输入岗位名称，重新输入新的薪资范围和备注
#4. **删除岗位**：输入岗位名称，确认后删除对应岗位
#5. **显示全部岗位**：按行打印所有岗位的完整信息
#6. **退出程序**：退出前自动保存所有数据


#设置存储位置名字
import json
def save(gwxx):
    with open('gwxx.json', 'w', encoding='utf-8') as f:
        json.dump(gwxx, f, ensure_ascii=False, indent=4)
#保存load_json函数，读取json文件内容,加载
def load_json():
    try:
        with open('gwxx.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    #主要程序
def main():
    continue_load = load_json()
    print("欢迎进入岗位信息系统！！！")
    while True:
        print("1. 新增岗位")
        print("2. 按名称查询岗位")
        print("3. 修改岗位薪资")
        print("4. 删除岗位")
        print("5. 显示全部岗位")
        print("6. 退出程序")
        choice = input("请输入操作编号：")
        if choice == '1':
            name=input("请输入岗位名称：")
            dw=input("请输入招聘单位：")
            dz=input("请输入工作地点：")
            salary=input("请输入薪资范围：")
            remark=input("请输入备注：")
            continue_load.append({"name":name,"dw":dw,"salary":salary,"dz":dz,"remark":remark})
            save(continue_load)
        elif choice == '2':
         name=input("请输入岗位名称：")
        found=False
        for gw in continue_load:
            if name == gw["name"]:
                print("岗位名称：",gw["name"])
                print("招聘单位：",gw["dw"])
                print("工作地点：",gw["dz"])
                print("薪资范围：",gw["salary"])
                print("备注：",gw["remark"])
                found=True
                break
        if not found:
            print("未找到该岗位信息！")
        if choice == '3':
            name=input("请输入要修改薪资的岗位名称：")
            found=False
            for gw in countinue_load:#查看是否存在该岗位
                if name == gw["name"]:
                    new_salary=input("请输入新的薪资范围：")
                    new_remark=input("请输入新的备注：")
                    gw["salary"]=new_salary
                    gw["remark"]=new_remark
                    save(continue_load)
                    print("岗位薪资修改成功！")
                    found=True
                    break
                if not found:
                    print("未找到该岗位信息！")
        elif choice == '4':
            name=input("请输入要删除的信息岗位名称：")
            found=False
            for i, gw in enumerate(continue_load):
                if name == gw["name"]:
                    continue_load.pop(i)
                    save(continue_load)
                    print("岗位信息删除成功！")
                    found=True
                    break
            if not found:
                print("未找到该岗位信息！")
        elif choice == '5':
            if not continue_load:
                print("暂无岗位信息！")
            else:
                for gw in continue_load:
                    print("岗位名称：",gw["name"])
                    print("招聘单位：",gw["dw"])
                    print("工作地点：",gw["dz"])
                    print("薪资范围：",gw["salary"])
                    print("备注：",gw["remark"])
                    print("--------------------")
        elif choice == '6':
            save(continue_load)
            print("数据已保存，程序退出！")
            break
        else:
            print("无效的操作编号，请重新输入！")
if __name__ == "__main__":
     main()
     