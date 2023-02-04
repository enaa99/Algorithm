exports.init = function () {
  global.io.on("connect", (socket) => {
    socket.on("c_init_boss", async function (data) {
      init_boss();
    });

    function boss_error_check(G) {
      if (!boss_exist) G.errormsg = "Cannot Join Game. Boss Doesn't Exist.";
      if (typeof bossroom_uids[G.id] == "undefined")
        G.errormsg = "User Doesn't Exist";
    }
    socket.on("c_room_info", async function (data) {
      var G = {};
      G.id = data.id;

      G.roomInfo = data.roomInfo;
      G.doorInfo = obj_interaction_list;
      room_information[data.id] = data.roomInfo;

      // if (data.roomInfo.toString() == "SampleScene") {

      //     G["doors"] = {};
      //     var doorkey = Object.keys(obj_interaction_list);
      //     var doorsvalue = Object.values(obj_interaction_list);
      //     for (var a = 0; a < doorkey.length; a++) {
      //         G["doors"][doorkey[a]] = {
      //             "info": doorsvalue[a]
      //         };
      //     }
      // }

      socket.emit("s_room_info", JSON.stringify(G));
      socket.broadcast.emit("s_room_info", JSON.stringify(G));
    });
    socket.on("c_check_room", async function (data) {
      var G = {};

      var friendList = data.test.toString();
      var splits = friendList.split(",");

      G["Friends"] = {};
      for (var i in splits) {
        G["Friends"][i] = {
          RoomInfo:
            room_information[splits[i]] != null
              ? room_information[splits[i]]
              : "LogOut",
        };
      }

      socket.emit("s_check_room", JSON.stringify(G));
    });
    socket.on("c_send_effect", async function (data) {
      var G = {};
      G["id"] = data.id;
      G["item"] = data.item;

      if (G.item.toString() == 1) effect_list[id] = G.item;
      else delete effect_list[id];

      effect_listing.push(effect_list);
    });
    socket.on("c_check_guild", async function (data) {
      var G = {};
      G.guild_name = data.guild_name;

      var guildList = data.test;
      var splits = guildList.toString().split(",");

      for (var i in splits) {
        guild_list[splits[i]] = G.guild_name;
      }

      G["guild"] = {};
      for (var i in splits) {
        G["guild"][i] = {
          Name: splits[i],
          RoomInfo:
            room_information[splits[i]] != null
              ? room_information[splits[i]]
              : "LogOut",
        };
      }

      socket.emit("s_check_guild", JSON.stringify(G));
    });
    socket.on("c_guild_apply", async function (data) {
      var G = {};

      G.id = data.id;
      G.guild_name = data.guild_name;

      apply_list[G.id] = G.guild_name;
    });
    socket.on("c_guild_accepted", async function (data) {
      var G = {};

      G.id = data.id;
      G.master_id = data.playerId;
      try {
        delete apply_list[G.id];
      } catch {}

      socket.to(uid_to_sid[G.id]).emit("s_guild_accepted", JSON.stringify(G));
    });
    socket.on("c_guild_rejected", async function (data) {
      var G = {};

      G.id = data.id;
      G.master_id = data.playerId;
      try {
        delete guild_list[G.id];
        delete apply_list[G.id];
      } catch {}

      socket.emit("s_guild_rejected", JSON.stringify(G));
      socket.to(uid_to_sid[G.id]).emit("s_guild_rejected", JSON.stringify(G));
      socket
        .to(uid_to_sid[G.master_id])
        .emit("s_guild_rejected", JSON.stringify(G));
    });
    socket.on("c_guild_listing", async function (data) {
      var G = {};
      var guild_name = data.guild_name.toString().split(",");
      var master_list = data.guild_id;

      G["guild_list"] = {};
      for (var i in guild_name) {
        if (master_list[i] != "") {
          guild_master_list[master_list[i]] = guild_name[i];
          console.log(master_list[i] + " list master");
          G["guild_list"][i] = {
            master_name: master_list[i],
            guild_name: guild_master_list[master_list[i]],
          };
        }
      }
    });
    socket.on("c_guild_list", async function (data) {
      var G = {};
      var guild_name = data.guild_name.toString().split(",");
      var master_list = data.guild_id;
      var myid = data.id;
      try {
        G.apply = apply_list[myid];
      } catch {}

      G["guild_list"] = {};
      for (var i in guild_name) {
        if (master_list[i] != "") {
          guild_master_list[master_list[i]] = guild_name[i];
          console.log(master_list[i] + " list master");
          G["guild_list"][i] = {
            master_name: master_list[i],
            guild_name: guild_master_list[master_list[i]],
          };
        }
      }

      socket.emit("s_guild_list", JSON.stringify(G));
      //socket.to(uid_to_sid[G.to_id]).emit('s_guild_list', JSON.stringify(G));
    });

    socket.on("c_delete_guild", async function (data) {
      var G = {};
      G.id = data.id;

      delete guild_list[G.id];
    });

    socket.on("c_add_friend", async function (data) {
      var G = {};

      G.id = data.id;
      G.to_id = data.playerId;

      socket.to(uid_to_sid[G.to_id]).emit("s_add_friend", JSON.stringify(G));
    });
    socket.on("c_accept_friend", async function (data) {
      var G = {};

      G.id = data.id;
      G.to_id = data.playerId;

      socket.to(uid_to_sid[G.to_id]).emit("s_accept_friend", JSON.stringify(G));
    });
    socket.on("c_delete_friend", async function (data) {
      var G = {};
      G.id = data.id;
      G.to_id = data.playerId;

      socket.to(uid_to_sid[G.to_id]).emit("s_delete_friend", JSON.stringify(G));
    });
    socket.on("c_check_status", async function (data) {
      var G = {};
      G.errormsg = "";
      G.id = data.id;

      G.uid_to_playerhp = uid_to_playerhp;
      G.boss_hp = boss_hp;

      socket.emit("s_check_status", JSON.stringify(G));
      socket.broadcast.emit("s_check_status", JSON.stringify(G));
    });
    socket.on("c_enter_bossroom", async function (data) {
      var G = {};
      G.errormsg = "";
      G.id = data.id;

      if (Object.keys(bossroom_uids).length >= max_players)
        G.errormsg = "Cannot Join Game. Player limit reached.";

      if (G.errormsg == "") {
        bossroom_uids[data.id] = true;
        uid_to_playerhp[data.id] = player_maxhp;
      }

      socket.emit("s_enter_bossroom", JSON.stringify(G));
    });
    socket.on("c_player_dead", async function (data) {
      var G = {};
      G.id = data.id;
      uid_to_playerhp[data.id] = 1000;
      G.player_hp = uid_to_playerhp[data.id];

      socket.emit("s_player_dead", JSON.stringify(G));
    });
    socket.on("c_exit_bossroom", async function (data) {
      var G = {};
      G.errormsg = "";
      G.id = data.id;

      if (uid_to_sid[G.id] != socket.id) return;

      boss_error_check(G);

      if (G.errormsg == "") {
        delete bossroom_uids[data.id];
        delete uid_to_playerhp[data.id];
      }

      socket.emit("s_exit_bossroom", JSON.stringify(G));
    });
    socket.on("c_attack_boss", async function (data) {
      try {
        if (boss_hp > 0) {
          var G = {};
          G.errormsg = "";
          G.id = data.id;
          if (uid_to_sid[G.id] != socket.id) return;

          boss_error_check(G);

          if (G.errormsg == "") {
            boss_hp -= player_atk;
            G.boss_hp = boss_hp;
          }

          socket.emit("s_attack_boss", JSON.stringify(G));
          socket.broadcast.emit("s_attack_boss", JSON.stringify(G));

          if (boss_hp <= 0) {
            boss_changestate(socket, 3, 0, {});
          }
        }
      } catch (err) {
        console.log(err);
      }
    });
    socket.on("c_attacked_by_boss", async function (data) {
      var G = {};
      G.errormsg = "";
      G.id = data.id;

      if (uid_to_sid[G.id] != socket.id) return;
      boss_error_check(G);

      if (G.errormsg == "") {
        uid_to_playerhp[data.id] -= boss_atk;
        G.player_hp = uid_to_playerhp[data.id];

        G.player_id = data.id;
      }

      socket.emit("s_attacked_by_boss", JSON.stringify(G));
      socket.broadcast.emit("s_attacked_by_boss", JSON.stringify(G));
    });
    socket.on("c_chat", async function (data) {
      var G = {};
      G.id = data.id;

      G.text = data.text;

      var Check = data.text.toString();
      var Checks = Check.split(" ");

      var valuest = Object.values(sid_to_uid);

      if (
        Checks[0].includes("/w") ||
        Checks[0].includes("/ㅈ") ||
        Checks[0].includes("/W")
      ) {
        if (G.id.toString() == Checks[1]) {
          G.text = "You can't send it to yourself";
          socket.emit("s_chat", JSON.stringify(G));
        } else if (uid_to_sid[Checks[1]]) {
          Check = Check.substring(Checks[1].length + 3);

          G.text = Check;

          socket.emit("s_whisper", JSON.stringify(G));
          socket.to(uid_to_sid[Checks[1]]).emit("s_whisper", JSON.stringify(G));
        } else {
          G.text = "User doesn't exist. Check Again";
          socket.emit("s_chat", JSON.stringify(G));
        }
      } else {
        socket.emit("s_chat", JSON.stringify(G));
        valuest.forEach((value) => {
          if (room_information[data.id] == room_information[value]) {
            socket.to(uid_to_sid[value]).emit("s_chat", JSON.stringify(G));
          }
        });
      }
    });
    socket.on("c_guild_chat", async function (data) {
      var G = {};
      G.id = data.id;

      G.text = data.text;

      var valuest = Object.values(sid_to_uid);

      socket.emit("s_guild_chat", JSON.stringify(G));
      valuest.forEach((value) => {
        if (guild_list[G.id] == guild_list[value]) {
          socket.to(uid_to_sid[value]).emit("s_guild_chat", JSON.stringify(G));
        }
      });
    });

    socket.on("c_auth", async function (data) {
      var sid = socket.id.toString();
      var uid = data.id.toString();

      room_information[uid] = data.roomInfo;
      sid_to_uid[sid] = uid;
      uid_to_sid[uid] = sid;

      setmovement(uid, 0, 0, 0, true);

      var G = { id: uid, roomInfo: data.roomInfo };

      G["others"] = {};

      var keys = Object.keys(uid_to_player_movement);
      var values = Object.values(uid_to_player_movement);

      // console.log("uid to player");
      // console.log(JSON.stringify(uid_to_player_movement));

      G["id"] = uid;

      for (var a = 0; a < keys.length; a++) {
        G["others"][keys[a]] = {
          l_x: values[a].x,
          l_y: values[a].y,
          l_z: values[a].z,
        };
      }
      G["doorInfo"] = obj_interaction_list;
      socket.emit("s_auth", JSON.stringify(G));
      socket.broadcast.emit("s_auth", JSON.stringify(G));
    });
    socket.on("c_move", function (data) {
      var G = {};
      //이 부분
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];

      G["anim"] = data.anim;
      G["l_x"] = data.l_x;
      G["l_y"] = data.l_y;
      G["l_z"] = data.l_z;
      G["r_w"] = data.r_w;
      G["r_x"] = data.r_x;
      G["r_y"] = data.r_y;
      G["r_z"] = data.r_z;
      G["walk"] = data.walk;
      G["jump"] = data.jump;
      G["delta"] = data.delta;

      //move_list.push(G);
      // socket.emit('s_move', JSON.stringify(G));
      // socket.broadcast.emit('s_move', JSON.stringify(G));
    });
    socket.on("c_stop", function (data) {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      G["l_x"] = data.x;
      G["l_y"] = data.y;
      G["l_z"] = data.z;

      setmovement(G["id"], data.x, data.y, data.z, true);

      socket.broadcast.emit("s_stop", JSON.stringify(G));
    });
    socket.on("c_char", function (data) {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      G["character"] = data.character;
      socket.broadcast.emit("s_char", JSON.stringify(G));
    });
    socket.on("c_test", function (data) {
      var G = {};
      G.id = data.id;

      if (uid_to_sid[G.id] != socket.id) return;

      G["id"] = sid_to_uid[socket.id];
      G["test"] = data.test;
      G["roomName"] = data.roomName;

      move_list.push(G);

      // console.log("moveList" + move_list);

      //     var valuest = Object.values(sid_to_uid);

      // valuest.forEach((value)=>{
      //     if(room_information[value] == room_information[G["id"].toString()]){
      //                 socket.to(uid_to_sid[value]).emit('s_test',JSON.stringify(G));
      //             }
      // })

      // for(let idx of valuest){
      //     if(room_information[idx] == room_information[sid_to_uid[socket.id]]){
      //         socket.to(uid_to_sid[idx]).emit('s_test',JSON.stringify(G));
      //     }

      // }
    });

    socket.on("c_test_2", function (data) {
      var G = {};

      G.idx = data.ObjectIDX;
      G.state = data.State;
      obj_interaction_list[G.idx] = G.state;

      G["doorInfo"] = obj_interaction_list;

      // var valuest = Object.values(sid_to_uid);
      // valuest.forEach((value) => {
      //     if (room_information[value] == "SampleScene") {

      //         socket.emit('s_test_2', JSON.stringify(G));
      //         socket.to(uid_to_sid[value]).emit('s_test_2', JSON.stringify(G));

      //     }
      // })
      socket.emit("s_test_2", JSON.stringify(G));
      socket.broadcast.emit("s_test_2", JSON.stringify(G));
    });
    socket.on("c_test_3", function (data) {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      G["test"] = data.test;
      socket.emit("s_test_3", JSON.stringify(G));
      socket.broadcast.emit("s_test_3", JSON.stringify(G));
    });
    socket.on("c_test_4", function (data) {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      G["test"] = data.test;
      socket.emit("s_test_4", JSON.stringify(G));
      socket.broadcast.emit("s_test_4", JSON.stringify(G));
    });
    socket.on("c_test_5", function (data) {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      G["test"] = data.test;
      socket.emit("s_test_5", JSON.stringify(G));
      socket.broadcast.emit("s_test_5", JSON.stringify(G));
    });
    socket.on("forceDisconnect", function () {
      disconnect(socket.id);
      socket.disconnect();
    });
    socket.on("c_disconnect", function () {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      socket.broadcast.emit("s_disconnect", JSON.stringify(G));
      disconnect(socket.id);
    });
    socket.on("disconnect", function () {
      var G = {};
      G["socket_id"] = socket.id;
      G["id"] = sid_to_uid[socket.id];
      socket.broadcast.emit("s_disconnect", JSON.stringify(G));
      disconnect(socket.id);
    });
  });
};
