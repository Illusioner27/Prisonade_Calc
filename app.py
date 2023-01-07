import streamlit as st

st.set_page_config(page_title="Prisonade Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('Spawn', 'Desert', 'Jungle','Ocean','Abyss'))
st.subheader("Which Block")
if dim=="Spawn":
     block = st.radio(
          "",
          ('Stone-Iron Mix', 'Iron-Diamond Mix', 'Diamond-Emerald Mix','Summit Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Stone-Iron Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of T3 Stone and Iron")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron ")
     elif block=="Iron-Diamond Mix":
          a=val*4
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Iron and Diamond")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond ")
     elif block=="Diamond-Emerald Mix":
          a=val*8
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diamond and Emerald")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diamond and Emerald ")
     else:
          dia=val*36
          eme=val*24
          iron=val*12
          if ((iron % 64)==0):
               st.header(f"You need {int(iron / 64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(iron / 64):,d} Stacks and {iron % 64} T3 Iron")
          if ((dia % 64)==0):
               st.header(f"You need {int(dia / 64):,d} Stacks of T3 Diamond")
          else:
               st.header(f"You need {int(dia/64):,d} Stacks and {dia%64} T3 Diamond")
          if ((eme % 64)==0):
               st.header(f"You need {int(eme / 64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(eme / 64):,d} Stacks and {eme % 64} T3 Emerald")
elif dim=="Grotto":
     block = st.radio(
          "",
          ('Diorite-Coal Mix','Coal-Lapis Mix','Lapis-Redstone Gem Mix','Grotto Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Diorite-Coal Mix':
          a=val*2
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diorite and Coal")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diorite and Coal ")
     elif block == "Coal-Lapis Mix":
          pri = val * 6
          fd=val*5
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Copper")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Gold")
          else:
               st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Gold")
     elif block == "Gold-Desert Gem Mix":
          a = val * 10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gold and Desert Gem")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Gold and Desert Gem ")
     else:
          ame = val * 24
          fd = val * 60
          pri = val * 40
          if ((ame % 64)==0):
               st.header(f"You need {int(ame/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Copper ")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Gold")
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Desert Gem")
elif dim=="Jungle":
     block = st.radio(
          "",
          ('Granite-Basalt Mix','Basalt-Coal Mix','Coal-Lapis Mix','Jungle Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Granite-Basalt Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Granite and Basalt")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Granite and Basalt ")
     elif block == "Coal-Lapis Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 and Coal and Lapis")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Coal and Lapis ")
     elif block == "Basalt-Coal Mix":
          fg=val*8
          hr=val*6
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Basalt")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Basalt ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Coal")
     else:
          mg = val * 40
          fg = val * 90
          hr = val * 60
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Basalt")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Basalt")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Coal ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Lapis")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Lapis ")
elif dim=="Ocean":
     block = st.radio(
          "",
          ('Prismarine- Pink Coral Mix','Pink Coral-Fire Coral Mix','Fire Coral-Blue Coral Mix','Ocean Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Prismarine- Pink Coral Mix':
          a=val*5
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gold and Prismarine and Pink Coral")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Prismarine and Pink Coral ")
     elif block == "Fire Coral-Blue Coral Mix":
          a = val * 13
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Fire Coral and Blue Coral")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Fire Coral and Blue Coral ")
     elif block == "Pink Coral-Fire Coral Mix":
          fg=val*8
          hr=val*7
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Pink Coral")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Pink Coral ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Fire Coral")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Fire Coral")
     else:
          mg = val * 48
          fg = val * 120
          hr = val * 78
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Pink Coral")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Pink Coral")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Fire Coral")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Fire Coral ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Blue Coral")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Blue Coral ")
elif dim=="Abyss":
     block = st.radio(
          "",
          ('Void Stone-Amethyst Mix','Amethyst-Hell Rock Mix','Hell Rock-Obsidian Mix','Abyss Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Void Stone-Amethyst Mix':
          a=val*6
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Void Stone and Amethyst")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Void Stone and Amethyst ")
     elif block == "Amethyst-Hell Rock Mix":
          fg=val*10
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Amethyst ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Hell Rock")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Hell Rock")
     elif block == "Hell Rock-Obsidian Mix":
          fg=val*15
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Hell Rock")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Hell Rock ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian")
     else:
          mg = val * 80
          fg = val * 184
          hr = val * 64
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of Amethyst")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Amethyst")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Hell Rock")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Hell Rock ")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ")
st.caption(f"Any Bugs ?")
st.caption(f"Message Stresso#6710 or Illusioner_#0127 On Discord ")
