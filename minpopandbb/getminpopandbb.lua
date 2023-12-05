local g = golly()

local maxticks = g.getstring("Enter maximum number of ticks to search: ", "1024")
local r = g.getrect()
local count, minT, minpop, minbbx, minbby, minbbt = 0, 0, g.getpop(), r[3], r[4], 0
local newpop = minpop

while count < tonumber(maxticks) do
    if count % 100 == 0 then
        g.show("T: " .. count .. "    Current pop: " .. newpop .. "    Current minimum pop: " .. minpop .. " at T = " .. minT .. ". Min box = {" .. minbbx .. ", " .. minbby .. "} at T = " .. minbbt .. ".  'q' to quit.")
        g.update()
        local cancel = 0
        for i = 1, 100 do
            local evt = g.getevent()
            if evt == "key q none" then
                cancel = 1
            end
        end
        if cancel == 1 then
            break
        end
    end
    g.run(1)
    count = count + 1
    newpop = g.getpop()
    if newpop < minpop then
        minpop = newpop
        minT = count
    end
    local r = g.getrect()
    if r[3] * r[4] < minbbx * minbby then
        minbbx, minbby, minbbt = r[3], r[4], count
    end
end

g.note("Finished scan of " .. count .. " ticks. Minimum population: " .. minpop .. " at T = " .. minT .. ". Min box = {" .. minbbx .. ", " .. minbby .. "} at T = " .. minbbt)
