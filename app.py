
import streamlit as st

st.set_page_config(page_title="MineUnWind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('River', 'Ranch', 'Port','Empire','Citadel'))
st.subheader("Which Block")
if dim=="River":
     block = st.radio(
          "",
          ('Stone-Iron Mix', 'Iron-Diamond Mix', 'Diamond-Emerald Mix','River Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Stone-Iron Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of  T3 Stone and Iron ({val} blocks)")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron ({val} blocks)")
     elif block == "Iron-Diamond Mix":
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Iron and Diamond  ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond ({a} blocks) ")
     elif block == "Diamond-Emerald Mix":
          a = val * 8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diamond and Emerald ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diamond and Emerald  ({a} blocks)")
     else:
          ame = val * 12
          fd = val * 36
          pri = val * 24
          if ((ame % 64)==0):
               st.header(f"You need {int(ame/64):,d} Stacks of T3 Iron ({ame} blocks)")
          else:
               st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Iron  ({ame} blocks)")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Diamond ({fd} blocks)")
          else:
               st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Diamond ({fd} blocks)")
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Emerald ({pri} blocks)")
          else:
               st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Emerald ({pri} blocks)")
if dim=="Ranch":
     block = st.radio(
          "",
          ('Granite-Coal Mix', 'Coal-Copper Mix', 'Copper-Redstone Mix','Ranch Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Granite-Coal Mix':
          a = val*4
          b = a % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of  T3 Stone and Iron ({a} blocks)")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron ({a} blocks)")
     elif block == "Coal-Copper Mix":
          pri = val * 6
          fd=val*5
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Coal ({pri} blocks)")
          else:
               st.header(f"You need {int(pri/64):,d} stacks and {pri%64} blocks of T3 Coal ({pri} blocks)")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Copper ({fd} blocks)")
          else:
               st.header(f"You need {int(fd/64):,d} stacks and {fd%64} blocks of T3 Copper ({fd} blocks)")
     elif block == "Copper-Redstone Mix":
          a = val * 10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Copper and Redstone ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Copper and Redstone ({a} blocks)")
     else:
          ame = val * 24
          fd = val * 60
          pri = val * 40
          if ((ame % 64)==0):
               st.header(f"You need {int(ame/64):,d} Stacks of T3 Coal ({ame} blocks)")
          else:
               st.header(f"You need {int(ame / 64):,d} Stacks and {ame % 64} T3 Coal ({ame} blocks) ")
          if ((fd % 64)==0):
               st.header(f"You need {int(fd/64):,d} Stacks of T3 Copper ({fd} blocks)")
          else:
               st.header(f"You need {int(fd / 64):,d} Stacks and {fd % 64} T3 Copper ({fd} blocks)")
          if ((pri % 64)==0):
               st.header(f"You need {int(pri/64):,d} Stacks of T3 Redstone ({pri} blocks)")
          else:
               st.header(f"You need {int(pri / 64):,d} Stacks and {pri % 64} T3 Redstone ({pri} blocks)")
elif dim=="Port":
     block = st.radio(
          "",
          ('Sandstone-Prismarine Mix','Prismarine-Oceanstone Mix','Oceanstone-Seashine Mix','Port Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone-Prismarine Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Sandstone and Prismarine ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Prismarine ({a} blocks)")
     elif block == "Prismarine-Oceanstone Mix":
          fg=val*8
          hr=val*6
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Prismarine ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Prismarine ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Oceanstone ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Oceanstone ({hr} blocks)")
     elif block == "Oceanstone-Seashine Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Oceanstone and Seashine ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Oceanstone and Seashine ({a} blocks)")
     else:
          mg = val * 40
          fg = val * 90
          hr = val * 60
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Prismarine ({mg} blocks)")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Prismarine ({mg} blocks)")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Oceanstone ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Oceanstone ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Seashine ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Seashine ({hr} blocks)")
elif dim=="Empire":
     block = st.radio(
          "",
          ('Moss Stone-Star Rock Mix','Star Rock-Aztez Relic Mix','Aztec Relic-Amethyst Mix','Empire Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Moss Stone-Star Rock Mix':
          a=val*5
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gold and Moss Stone and Star Rock ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Moss Stone and Star Rock ({a} blocks)")
     elif block == "Star Rock-Aztez Relic Mix":
          fg=val*8
          hr=val*7
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Star Rock ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Star Rock ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Aztec Relic ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Azteec Relic ({hr} blocks)")
     elif block == "Aztec Relic-Amethyst Mix":
          a = val * 13
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Aztec Relic and Amethyst ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Aztec Relic and Amethyst ({a} blocks)")
     else:
          mg = val * 48
          fg = val * 120
          hr = val * 78
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of T3 Star Rock ({mg} blocks)")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Star Rock ({mg} blocks)")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Aztec Relic ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Aztec Relic ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Amethyst ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Amethyst ({hr} blocks)")
elif dim=="Citadel":
     block = st.radio(
          "",
          ('Marble-Purpur Mix','Purpur-Magma Mix','Magma-Obsidian Mix','Citadel Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Marble-Purpur Mix':
          a=val*6
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Marble and Purpur ({a} blocks)")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Marble and Purpur ({a} blocks)")
     elif block == "Purpur-Magma Mix":
          fg=val*10
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Purpur ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Purpur ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Magma ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Magma ({hr} blocks)")
     elif block == "Magma-Obsidian Mix":
          fg=val*15
          hr=val*8
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ({hr} blocks)")
     else:
          mg = val * 80
          fg = val * 184
          hr = val * 64
          if ((mg % 64)==0):
               st.header(f"You need {int(mg/64):,d} Stacks of Purpur ({mg} blocks)")
          else:
               st.header(f"You need {int(mg / 64):,d} Stacks and {mg % 64} T3 Purpur ({mg} blocks)")
          if ((fg % 64)==0):
               st.header(f"You need {int(fg/64):,d} Stacks of T3 Magma ({fg} blocks)")
          else:
               st.header(f"You need {int(fg / 64):,d} Stacks and {fg % 64} T3 Magma ({fg} blocks)")
          if ((hr % 64)==0):
               st.header(f"You need {int(hr/64):,d} Stacks of T3 Obsidian ({hr} blocks)")
          else:
               st.header(f"You need {int(hr / 64):,d} Stacks and {hr % 64} T3 Obsidian ({hr} blocks)")
st.caption(f"Any Bugs ?")
st.caption(f"Message Illusioner_ on discord!")
