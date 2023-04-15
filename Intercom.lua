-- Client side stuff
RegisterNetEvent('qb-policejob:client:Intercom')
AddEventHandler('qb-policejob:client:Intercom', function(callsign, job, msg)
    TriggerServerEvent('qb-policejob:server:Intercom', callsign, job, msg)
end)

-- Server side stuff
QBCore.Commands.Add("ic", "Send A Message To the Emergency Intercom", {{name = "message", help = "Message"}}, true, function(source, args)
    local src = source
    local Player = QBCore.Functions.GetPlayer(src)
    local callsign = Player.PlayerData.metadata["callsign"]
    local job = Player.PlayerData.job.name
    local msg = table.concat(args, " ")
  
  
    if job == "police" or job == "ambulance" or job == 'highway' or job == 'bcso' then
      local colour
      if job == "police" or job == 'highway' or job == 'bcso' then
        colour = "information"
      else
        colour = "error"
      end
      
      if Player.PlayerData.job.onduty then
        TriggerClientEvent('qb-policejob:client:Intercom', -1, callsign, colour, msg)
      else
        TriggerClientEvent('QBCore:Notify', src, "You are not on duty!", "error", 5000)
      end
    end
end)

RegisterServerEvent('qb-policejob:server:Intercom', function(callsign, colour, msg)
    local src = source
    local Player = QBCore.Functions.GetPlayer(src)
    if Player ~= nil and
      (((Player.PlayerData.job.name == "police" or Player.PlayerData.job.name == "highway" or Player.PlayerData.job.name == "fib" or Player.PlayerData.job.name == "bcso") or Player.PlayerData.job.name == "ambulance") and
        Player.PlayerData.job.onduty) then
      TriggerClientEvent('chatMessage', src, "Intercom | " .. callsign, colour, msg)
    end
end)
  