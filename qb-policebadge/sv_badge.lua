local QBCore = exports['qb-core']:GetCoreObject()

RegisterServerEvent('badge:open')
AddEventHandler('badge:open', function(ID, targetID, type, result)
	local Player = QBCore.Functions.GetPlayer(ID)
	local data = {
		name = Player.PlayerData.charinfo.firstname.." "..Player.PlayerData.charinfo.lastname,
		job = Player.PlayerData.job.name,
		cid = Player.PlayerData.citizenid,
		callsign = MySQL.scalar.await('SELECT callsign FROM drx_mdw_officers WHERE citizenid = ?', {Player.PlayerData.citizenid}),
        rankName = Player.PlayerData.job.grade.name,
		rank = Player.PlayerData.job.grade.level
	}
	
	TriggerClientEvent('badge:open', targetID, data)
	TriggerClientEvent('badge:shot', targetID, ID)

	-- QBCore.Functions.TriggerCallback('qb-policebadge:server:getMDWImage', function(result)
	-- 	if result then 
	-- 	  print(result)
	-- 	else
	-- 	  print("No info in MDW for this person")
	-- 	end
	-- end)

end)

QBCore.Functions.CreateUseableItem('specialbadge', function(source, item)
    TriggerClientEvent('badge:openPD', source, true)
end)

-- QBCore.Functions.CreateCallback("qb-policebadge:server:getMDWImage", function(source, cb)
--     local src = source
--     local Player = QBCore.Functions.GetPlayer(src)
--     MySQL.query('SELECT image, alias FROM drx_mdw_officers WHERE citizenid = ?', {Player.PlayerData.citizenid}, function(result)
--         if result[1] then
--             cb(result[1])
--         else
--             cb(false)
--         end
--     end)
-- end)