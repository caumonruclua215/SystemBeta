import discord
import asyncio
import random
from discord.ext import commands

client=commands.Bot(command_prefix=".")
server=discord.Server(id="478247509328920576")
##############################
Player={}
Alive=[]
Dead=[]
##############################
Area={
	"giảng-đường":[], 
	"hành-lang":[], 
	"lớp-học":[], 
	"phòng-thực-hành":[], 
	"phòng-thể-chất":[], 
	"thư-viện":[], 
	"căn-tin":[]
	}
##############################
Arena=[
	"giảng-đường", 
	"hành-lang", 
	"lớp-học", 
	"phòng-thực-hành", 
	"phòng-thể-chất", 
	"thư-viện", 
	"căn-tin"
	]
##############################
ItemArena={
	"hành-lang" : [
		["Mảnh Kính", 15], 
		["Ống Sắt Rỗng", 10], 
		["Tấm Sắt", 8], 
		["Đá", 15]
		],
	"lớp-học" : [
		["Giấy Dày", 15], 
		["Bút Chì", 10], 
		["Gỗ", 8],
		["Ống Sắt Rỗng", 10], 
		["Tấm Sắt", 8]
		],
	"phòng-thực-hành" : [
		["Mảnh Kính", 10],
		["Búa", 10],
		["Mạch Máy Tính", 15],
		["Dây Điện", 15],
		["Tia Laser", 10],
		["Tấm Sắt", 8],
		["Kính Lúp", 10]
		],
	"thư-viện" : [
		["Sách Công Thức", 6]
		],
	"căn-tin": [
		["Pin", 15],
		["Dao", 10],
		["Bật Lửa", 10],
		["Đá Mài", 8],
		["Nước Khoáng", 20],
		["Mì Ăn Liền", 15],
		["Chocolate", 10],
		["Bánh Mì", 15],
		["Sữa", 10],
		["Bột Cà Phê", 10],
		]
}
##############################
ItemCraft = {
	"Bản Vẽ" :
		["Giấy Dày", "Bút Chì"],
	"Màn Hình" : 
		["Mảnh Kính", "Màn Hình Hỏng"],
	"Mạch Điện" : 
		["Dây Điện", "Mạch Điện Hỏng"],
	"Mạch Điện Cảm Biến" : 
		["Bản Vẽ", "Mạch Điện"],
	"Máy Cảm Biến" : 
		["Mạch Điện Cảm Biến", "Màn Hình"],
	"Ống Kính Lúp" : 
		["Ống Sắt Rỗng", "Kính Lúp"],
	"Tia Laser Mạnh" : 
		["Tia Laser", "Ống Kính Lúp"],
	"Vật Kính" : 
		["Mảnh Kính", "Tia Laser Mạnh"],
	"Thân Ống Kính" : 
		["Ống Kính Lúp", "Vật Kính"],
	"Thân Ống Kính Hiển Vi" : 
		["Bản Vẽ", "Thân Ống Kính"],
	"Kính Hiển Vi" : 
		["Mảnh Kính", "Thân Ống Kính Hiển Vi"],
	"Mạch Điện Đồng Hộ" : 
		["Bản Vẽ", "Mạch Điện"],
	"Đồng Hồ" : 
		["Mạch Điện Đồng Hồ", "Màn Hình"],
	"Tro" : 
		["Giấy Dày", "Bật Lửa"],
	"Mạch Điện Kiếm Công Nghệ" : 
		["Bản Vẽ", "Mạch Điện"],
	"Kiếm" : 
		["Mảnh Sắt", "Đá Mài"],
	"Kiếm Công Nghệ" : 
		["Kiếm", "Mạch Điện Kiếm Công Nghệ"],
	"Kiếm Laser" : 
		["Kiếm", "Tia Laser Mạnh"],
	"Chùy Sắt" : 
		["Gỗ", "Mảnh Sắt"],
	"Côn Sắt" : 
		["Gỗ", "Ống Sắt Rỗng"],
	"Đại Đao" :
		["Côn Sắt",  "Mảnh Sắt"],
	"Dao Sắt Nhọn" : 
		["Dao", "Đá Mài"],
	"Chùy Dài" : 
		["Côn Sắt", "Chùy Sắt"],
	"Song Quải" : 
		["Gỗ", "Gỗ"],
	"Nước Sôi" : 
		["Nước Khoáng", "Bật Lửa"],
	"Mì Ăn Liền" : 
		["Mì Gói", "Nước Sôi"],
	"Bột Cacao" : 
		["Chocolate", "Dao"],
	"Cacao Nóng" : 
		["Bột Cacao", "Nước Sôi"],
	"Cà Phê Nóng" :
		["Bột Cà Phê", "Nước Sôi"],
	"Bánh Mì Nóng" : 
		["Bóng Mì", "Bật Lửa"],
	"Bánh Mì Nhân Chocolate" : 
		["Bánh Mì Nóng", "Chocolate"],
}
##############################
UseItem = {
	"Nước Khoáng" : {
		"Energy" : 10
	},
	"Sữa" : {
		"Energy" : 15
	},
	"Mì Ăn Liền" : {
		"Energy" : 20
	},
	"Cacao Nóng" : {
		"Energy" : 30
	},
	"Cà Phê Nóng" : {
		"Energy" : 30
	},
	"Bánh Mì Nóng" : {
		"Energy" : 25
	},
	"Bánh Mì Nhân Chocolate" : {
		"Energy" : 35
	},
}
##############################
ItemEquip = {
	"Kiếm" : {
		"Str" : 10,
		"Agi" : 0
	},
	"Kiếm Công Nghệ" : {
		"Str" : 25,
		"Agi" : 0
	},
	"Kiếm Laser" : {
		"Str" : 25,
		"Agi" : 0
	},
	"Chùy Sắt" : {
		"Str" : 15,
		"Agi" : -5
	},
	"Chùy Dài" : {
		"Str" : 35,
		"Agi" : -10
	},
	"Côn Sắt" : {
		"Str" : 5,
		"Agi" : 5
	},
	"Đại Đao" : {
		"Str" : 20,
		"Agi" : 5
	},
	"Song Quải" : {
		"Str" : 20,
		"Agi":0
	},
	"Dao Sắt Nhọn" : {
		"Str" : 20,
		"Agi":0
	}
}
##############################
@client.event
async def on_ready():
	print("Bot Is Ready!!!\n-------------------------")
##############################
Day=[1]
Hour=[6]
Minute=[0]

@client.event
async def time():
	day=1
	hour=6
	minute=0
	alive=len(Alive)
	if alive==6:
		while not alive==0:
			if hour in range(6,22):
				await asyncio.sleep(1)
				minute+=1
				Minute.clear()
				Minute.append(minute)
				if minute == 60:
					minute = 0
					hour += 1
					Hour.clear()
					Hour.append(hour)
			elif hour in range(22,6):
				await asyncio.sleep(1)
				minute+=2
				Minite.clear()
				Minute.append(minute)
				if minute == 60:
					minute = 0
					hour += 1
					Hour.clear()
					Hour.append(hour)
					if hour == 24:
						hour = 0
						day += 1
						Day.clear()
						Day.append(day)
##############################
@client.event
async def on_member_join(member):
	role=discord.utils.get(member.server.roles, name="Viewer")
	await client.add_roles(member, role)
##############################
@client.event
async def on_message(message):
	User=message.author
	Name=message.author.name
	Id=message.author.id
	Mention=message.author.mention
	Channel=message.channel	
	Channelid=message.channel.id
	Channelname=message.channel.name
	if message.content.startswith(".play"):
		if not Channelname == "phòng-chờ":
			await client.send_message(Channel, "Vui Lòng Tiến Vào #phòng-chờ  Để Bắt Đầu Đăng Ký Tham Gia Trò Chơi!!!")
		elif Channelname == "phòng-chờ":
			if User in Player:
				await client.send_message(Channel, "**{} Đã Đăng Ký Tham Gia Trò Chơi!!!\nVui Lòng Chờ Thêm Người Chơi Để Bắt Đầu Trò Chơi**". format(Mention))
			if not User in Player:
				player=len(Player)
				if player > 5:
					await client.send_message(Channel, "Trò Chơi Đã Bắt Đầu!!!\nVui Lòng Chờ Trò Chơi Kết Thúc Để Tiến Hành Đăng Ký Tham Gia Trò Chơi Tiếp Theo!!!")
				else:
					Roler=[]
					Roler.append(User)
					Alive.append(Name)
					Player[Name]={}
					Player[Name].update(
				Info={},
				Equip=None,
				Localtion=[], 
				Bag=[],
				Bag2=[],
				Friend=[],
				Form="Man",
				Channel=User,
				Id=Id
				)
					Player[Name]["Info"].update(
				Str=10,
				Int=10,
				Agi=10,
				Energy=100,
				)
					play=len(Player)
					print(Player)
					await client.send_message(Channel, "Chúc Mừng {} Đã Đăng Ký Tham Gia Trò Chơi Thành Công!!!\nSố Người Tham Gia : {}/6". format(Mention, play))
					if play == 6:
						x=0
						while x < 6:
							roler=Roler[x]
							role=discord.utils.get(message.server.roles, name="Roler")
							await client.add_roles(roler, role)
							x+=1
						await client.send_message(Channel, "Số Người Tham Gia Đã Đủ!!!")
						await client.send_message(Channel, "***```Trò Chơi Bắt Đầu!!!```***")
##############################
	if Name in Dead:
		role=discord.utils.get(message.server.roles, name="Roler")
		await client.remove_roles(User, role)
	if Name in Alive:
##############################
#Hệ Thống Định Vị
		bot= "483667963778695169"
		if not Id == bot:
			if Channelname in Arena:
				Player[Name]["Localtion"].clear()
				Player[Name]["Localtion"].append(Channelname)
				Player[Name]["Localtion"].append(Channel)
##############################
#Hệ thống Định Vị Số Người Chơi Trong Khu Vực
		if str(Channelname) in Arena:
			arena = 0
			while arena < 7:
				if Name in Area[Arena[arena]]:
					Area[Arena[arena]].remove(Name)
				elif not Name in Area[Arena[arena]]:
					arena+=1
					if arena == 7:
						Area[Player[Name]["Localtion"][0]].append(User)
##############################
#Hệ Thống Thông Tin
		if message.content.startswith(".info"):
			channel=message.content[5:]
			channels=message.content[99:]
			friend=len(Player[Name]["Friend"])
			local=len(Player[Name]["Localtion"])
			embed = discord.Embed(
				title=Name, 
				description="Thông Tin :", 
				color=0x990000)
			embed.add_field(
				name="Sức Mạnh :", 
				value=Player[Name]["Info"]["Str"], 
				inline=True)
			embed.add_field(
				name="Trí Tuệ :", 
				value=Player[Name]["Info"]["Int"], 
				inline=True)
			embed.add_field(
				name="Nhanh Nhẹn :", 
				value=Player[Name]["Info"]["Agi"], 
				inline=True)
			embed.add_field(
				name="Thể Lực :", 
				value=Player[Name]["Info"]["Energy"], 
				inline=True)
			embed.add_field(name="Trang Bị :", value=Player[Name]["Equip"])
			if local == 0:
				embed.add_field(
				name="Địa Điểm :", 
				value="None.", 
				inline=True)
			else:
				embed.add_field(
					name="Địa Điểm :", 
					value=Player[Name]["Localtion"][0], 
					inline=True)
			if friend == 0:
				embed.add_field(
					name="Bạn Bè :", 
					value="None.", 
					inline=True)
			else:
				embed.add_field(
					name="Bạn Bè :", 
					value=Player[Name]["Friends"], 
					inline=True)
			embed.add_field(
					name="Dạng :",
					value=Player[Name]["Form"])
			if channel == channels:
				await client.send_message(User, embed=embed)
			elif channel == "p":
				await client.send_message(Channel, embed=embed)
##############################
#Hệ Thống Giết Người Của Killer
		if message.content.startswith(".kill"):
			Target=message.content[6:]
			Role=discord.utils.get(
			server.roles, 
			name="Roler"
			)
			if Target == Name:
				await client.send_message(client.get_channel(id="496025299645890571"), "{} Đã Tự Sát!!!". format(Name))
				Alive.remove(Name)
				Dead.append(Name)
				await client.remove_roles(User, Role)
				if len(Player[Taget]["Bag2"]) > 0:
					Item[Player[Killer]["Localtion"][0]].extend(Player[Killer]["Bag2"])
			if Target in Alive:
				if not Player[Target]["Localtion"][0] == Player[Name]["Localtion"][0]:
					await client.send_message(Channel, "**{} Hiện Không Ở Cùng Khu Vực Với Bạn!!!**". format(Target))
				else:
					k=Player[Name]["Info"]
					t=Player[Target]["Info"]
					str1=k["Str"]-t["Str"]
					int1=k["Int"]-t["Int"]
					agi1=k["Agi"]-t["Agi"]
					area=len(Area[Player[Target]["Localtion"][0]])
					kill=int((str1+int1+agi1)*0.5)+50
					str2=t["Str"]-k["Str"]
					int2=t["Int"]-k["Int"]
					agi2=t["Agi"]-k["Agi"]
					
					reveal=int((str2+int2+agi2)*0.5)+int(area+20)
					p=random.randrange(0,100)
					if not p in range(kill):
						if p in range(reveal):
							await client.send_message(Player[Target]["Localtion"][1], "**{} Bị Một Kẻ Giấu Mặt Tấn Công!!!\nNhưng {} Đã Phản Công Lại!!!**". format(Target, Target))
							await client.send_message(User, "Tấn Công {} Thất Bại!!!". format(Target))
							await asyncio.sleep(60)
							if not Target in Dead:
								await client.send_message(Player[Target]["Channel"], "**Trong Lúc Phản Kháng Bạn Đó Vô Tình Nhìn Thấy Mặt Kẻ Giết Người Kia!!!\nHình Như Hắn Là {}!!!**". format(Name))
						else:
							await client.send_message(Player[Target]["Localtion"][1], "**{} Bị Một Kẻ Giấu Mặt Tấn Công!!!\nNhưng {} Đã Phản Công Lại!!!**". format(Target, Target))
							await client.send_message(User, "Tấn Công {} Thất Bại!!!". format(Target))
					else:
						await client.send_message(Player[Target]["Localtion"][1], "{} Đã Bị Giết Bởi Kẻ Giấu Mặt!!!". format(Target))
						Alive.remove(Target)
						Dead.append(Target)
						Player[Name].update(Form="Killer")
						if len(Player[Target]["Bag2"]) > 0:
							Item[Player[Target]["Localtion"][0]].extend(Player[Taget]["Bag2"])
						await client.send_message(client.get_channel(id="496025299645890571"), "{} Đã Chết Vì Bị Giết!!!". format(Target))
##############################
		if message.content.startswith(".search"):
			if len(Player[Name]["Bag"]) >= 10:
				await client.send_message(Channel, "Túi Đồ Của {} Đã Đầy!!!". format(Name))
			else:
				if Channelname in ItemArena:
					search=random.randrange(1,101)
					Player[Name]["Info"]["Energy"] -= 2
					print(search)
					if len(ItemArena[Channelname])>0:
						await asyncio.sleep(5)
						if search in range(1,81):
							item=random.choice(ItemArena[Channelname])
							it=item.copy()
							it[1]=1
							Player[Name]["Bag"].append(it[0])
							Player[Name]["Bag2"].append(it)
							print(Player[Name]["Bag2"])
							await client.send_message(Channel, "**{} Đã Nhặt Được {}!!!**". format(Name, item[0]))
							i=ItemArena[Channelname].index(item)
							ItemArena[Channelname][i][1]-=1
					
							if ItemArena[Channelname][i][1] == 0:
								ItemArena[Channelname].remove(item)
						else:
							await client.send_message(Channel, "**{} Không Tìm Được Gì Cả!!!**". format(Name))
					else:
						await client.send_message(Channel, "Khu Vực Này Không Có Gì Để Tìm Kiếm!!!")
##############################
#Hệ Thống Bạn Bè
		if message.content.startswith(".af"):
			Friend=message.content[4:]
			friend=len(Player[Name]["Friend"])
			if not Friend in Alive:
				await client.send_message(Channel, "**Người Chơi {} Không Tồn Tại!!!**". format(Friend))
			else:
				if not Friend==Name:
					if friend > 1:
						await client.send_message(Channel, "**Danh Sách Bạn Bè Của Bạn Đã Đầy!!!**")
					else:
						await client.send_message(Channel, "**{} Đã Trở Thành Bạn Của Bạn!!!**". format(Friend))
						Player[Name]["Friend"].append(Friend)

		if message.content.startswith(".rf"):
			Friend=message.content[4:]
			if not Friend in Player[Name]["Friend"]:
				await client.send_message(Channel, "**{} Không Phải Là Bạn Của Bạn!!!**". format(Friend))
			else:
				await client.send_message(Channel, "**Bạn Đã Hủy Kết Bạn Với {} Thành Công!!!**". format(Friend))
				Player[User]["Friend"].remove(Friend)
##############################
		if message.content.startswith(".bag"):
			Bag=len(Player[Name]["Bag"])
			bag=0
			if Bag >= 1:
				embed = discord.Embed(title=Name, description="Túi Đồ :", color=0x990000)
				while bag <= (Bag-1):
					
					embed.add_field(name=(Player[Name]["Bag"][bag]),value="1",inline= False)
					bag+=1
				
				await client.send_message(User, embed=embed)
			else:
				await client.send_message(Channel, "{} Không Có Vật Phẩm Nào Trong Túi Đồ Cả!!!". format(Name))
		if message.content.startswith(".rm"):
			print(ItemArena[Channelname])
			item=message.content[4:]
			if item in Player[Name]["Bag"]:
				i=int(Player[Name]["Bag"].index(item))
				Player[Name]["Bag"].remove(item)
				await client.send_message(Channel, "{} Đã Vứt Bỏ Vật Phẩm {}!!!". format(Name, item))
				it=Player[Name]["Bag2"].pop(i)
				ItemArena[Channelname].extend(it)
				Player[Name]["Bag2"].pop(i)	
##############################
		if message.content.startswith(".ct"):
			page=int(message.content[4:])
			i=list(ItemCraft.keys())
			if ["Sách Công Thức", 1] in Player[Name]["Bag"]:
				if page==3:
					embed=discord.Embed(title="Sách Công Thức :", description="Thiết Bị", color=0x990000)
					item=0
					while item <= 14:
						embed.add_field(name=i[item], value="Yêu Cầu {} Để Chế Tạo!!!". format(ItemCraft[i[item]]), inline=False)
						item += 1
					
					await client.send_message(Channel, embed=embed)
				elif page==2:
					item=15
					embed=discord.Embed(title="Sách Công Thức :", description="Vũ Khí", color=0x990000)
					while item<=23:
						embed.add_field(name=i[item], value="Yêu Cầu {} Để Chế Tạo!!!". format(ItemCraft[i[item]]), inline=False)
						item+=1
					await client.send_message(message.channel, embed=embed)
				elif page==1:
					item=24
					embed=discord.Embed(title="Sách Công Thức :", description="Thức Ăn", color=0x990000)
					while item<=30:
						embed.add_field(name=i[item], value="Yêu Cầu {} Để Chế Tạo!!!". format(ItemCraft[i[item]]), inline=False)
						item+=1
					await client.send_message(message.channel, embed=embed)
##############################
		if message.content.startswith(".craft"):
			item=message.content[7:]
			item1 = ItemCraft[item][0]
			item2 = ItemCraft[item][1]
			if item in ItemCraft:
				if item1 in Player[Name]["Bag"]:
					if item2 in Player[Name]["Bag"]:
						Player[Name]["Bag"].remove(item1)
						Player[Name]["Bag"].remove(item2)
						Player[Name]["Bag"].append(item)
						await client.send_message(Channel, "{} Đã Chế Tạo Vật Phẩm {} Thành Công!!!". format(Name, item))
##############################
		if message.content.startswith(".use"):
			item = message.content[5:]
			Energy=Player[Name]["Info"]["Energy"]
			if item in Player[Name]["Bag"]:
				if item in UseItem:
					Player[Name]["Info"].update(Energy=Energy+UseItem[item]["Energy"])
					await client.send_message(Channel, "{} Đã Dùng {} Để Hồi {} Năng Lượng". format(Name, item, (UseItem[item]["Energy"])))
					Player[Name]["Bag"].remove(item)
##############################
		if message.content.startswith(".equip"):
			item=message.content[7:]
			Str=Player[Name]["Info"]["Str"]
			Agi=Player[Name]["Info"]["Agi"]
			if item in Player[Name]['Bag']:
				if item in ItemEquip:
					Player[Name]["Info"].update(Str=Str+ItemEquip[item]["Str"])
					Player[Name]["Info"].update(Agi=Agi+ItemEquip[item]["Agi"])
					Player[Name]['Bag'].remove(item)
					Player[Name].update(Equip=item)
					await client.send_message(Channel, "{} Đã Trang Bị Vật Phẩm!!!". format(Name))
		
		if message.content.startswith(".unequip"):
			if Player[Name]["Equip"] in ItemEquip:
				Player[Name]["Bag"].append(Player[Name]["Equip"])
				Str=ItemEquip[Player[Name]["Equip"]]["Str"]
				Agi=ItemEquip[Player[Name]["Equip"]]["Agi"]
				Player[Name]["Info"].update(
				Str=Player[Name]["Info"]["Str"]-Str,
				Agi=Player[Name]["Info"]["Agi"]-Agi
				)
				await client.send_message(Channel, "{} Đã Tháo Trang Bị!!!". format(Name))
				Player[Name]["Equip"] = None
##############################
		if message.content.startswith(".train"):
			bt=str(message.content[7:])
			if Channelname=="phòng-thể-chất":
				if bt == "Hít Đất":
					await asyncio.sleep(10)
					Player[Name]["Info"].update(
					Str=Player[Name]["Info"]["Str"]+4)
					await client.send_message(Channel, "{} Đã Hoàn Thành Bài Tập!!!". format(Name))
				elif bt == "Chạy Nước Rút":
					await asyncio.sleep(10)
					Player[Name]["Info"].update(
					Agi=Player[Name]["Info"]["Agi"]+4)
					await client.send_message(Channel, "{} Đã Hoàn Thành Bài Tập!!!". format(Name))
				else:
					await asyncio.sleep(10)
					Player[Name]["Info"].update(
					Agi=Player[Name]["Info"]["Agi"]+2,
					Str=Player[Name]["Info"]["Str"]+2)
					await client.send_message(Channel, "{} Đã Hoàn Thành Bài Tập!!!". format(Name))
##############################
		if message.content.startswith(".read"):
			if Channelname=="thư-viện":
				#await asyncio.sleep(10)
				Player[Name]["Info"].update(
					Int=Player[Name]["Info"]["Int"]+4)
				await client.send_message(Channel, "{} Tăng 4 Điểm Trí Tuệ Sau Khi Đọc Sách!!!". format(Name))
##############################
	Vote=[]
	if Day[0] >= 2:
		if Hour[0] == 5:
			await client.send_message(Channel, "1 Tiếng Nữa Sẽ Tới Giờ Phán Quyết!!!")
			if Minute[0] == 30:
				await client.send_message(Channel, "30 Phút Nữa Sẽ Tới Giờ Phán Quyết!!!\nVui Lòng Tập Hợp Tại Khu Giảng Đường Trước 6 Giờ!!!")
		if Hour[0] < 8:
			if Hour[0] >= 6:
				if not Player[Name]["Localtion"][0] == "giảng-đường":
					Alive.remove(Name)
					Dead.append(Name)
					await client.send_message(client.get_channel(id="496025299645890571"), "{} Đã Bị Xử Tử Vì Hoạt Động Ngoài Khi Vực Giảng Đường!!!". format(Name))
				else:
					voter=[]
					if message.content.startswith(".vote"):
						if Name in voter:
							await client.send_message(Channel, "{} Đã Hết Lượt Vote!!!". format(Name))
						if not Name in voter:		
							voter.append(Name)
							
							target=message.content[6:]
							Vote.append(Target)
		if Hour[0] == 8:
			Vote.sort()
			kill=Vote[0]
			Alive.remove[kill]
			Dead.append[kill]
			await client.send_message(client.get_channel(id="496025299645890571"), "Tổng Kết!!!\n{} Là Người Có Nhiều Phiếu Nhất!!!\nKết Quả...SÁT!!!". format(kill))
		
	if len(Dead) >= 1:
		if len(Alive) == 2:
			if Alive[0] in Player[Alive[1]]["Friend"]:
				if Alive[1] in Player[Alive[0]]["Friend"]:
					await client.send_message(Channel, "Chúc Mừng {} Và {} Là Hai Người Chơi Cuối Cùng Còn Sống Sót!!!\n***```Game Over!!!***```". format(Alive[1], Alive[0]))
					Alive.clear()
		if len(Alive) == 1:
			await client.send_message(Channel, "Chúc Mừng {} Là Người Chơi Cuối Cùng Còn Sống Sót!!!\n***```Game Over!!!```***". format(Alive[0]))
			Alive.clear()
		
					



client.loop.create_task(time())
client.run(process.env.BOT_TOKEN)
