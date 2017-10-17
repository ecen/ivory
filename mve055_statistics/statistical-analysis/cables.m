cla
hold off

powerCables = [169, 199, 192, 241, 199, 200, 252, 201, 200];
bananCables = [32, 112, 112, 58, 58, 57, 113, 112, 113, 112, 112, 112, 63, 59, 58, 59, 58, 54];

ranksum(powerCables, bananCables)

lengths = [119, 32, 118, 112, 112, 58, 58, 152, 57, 169, 108, 199, 180, 192, 192, 192, 130, 203, 113, 201, 112, 113, 112, 112, 112, 210, 63, 59, 58, 59, 241, 199, 58, 54, 200, 199, 120, 252, 196, 201, 200, 118, 109, 120, 139, 129, 42, 53, 95, 151, 151];
diameters = [6.366197723675814, 3.183098861837907, 5.411268065124442, 4.7746482927568605, 4.45633840657307, 2.864788975654116, 3.183098861837907, 5.411268065124442, 3.183098861837907, 7.321127382227186, 5.411268065124442, 7.321127382227186, 5.092958178940651, 7.321127382227186, 4.7746482927568605, 7.639437268410976, 3.5014087480216975, 5.729577951308232, 3.819718634205488, 4.7746482927568605, 4.45633840657307, 4.7746482927568605, 4.45633840657307, 4.7746482927568605, 4.45633840657307, 4.138028520389279, 3.819718634205488, 4.7746482927568605, 2.864788975654116, 2.864788975654116, 6.684507609859605, 7.002817496043395, 3.5014087480216975, 3.183098861837907, 6.684507609859605, 4.7746482927568605, 5.729577951308232, 7.321127382227186, 4.7746482927568605, 7.002817496043395, 7.002817496043395, 4.7746482927568605, 5.092958178940651, 5.092958178940651, 5.092958178940651, 5.411268065124442, 5.411268065124442, 5.411268065124442, 5.092958178940651, 3.183098861837907, 3.5014087480216975];

% --- Banana ---
BananaL = [32, 112, 112, 58, 58, 57, 113, 112, 113, 112, 112, 112, 63, 59, 58, 59, 58, 54]
BananaD = [3.183098861837907, 4.7746482927568605, 4.45633840657307, 2.864788975654116, 3.183098861837907, 3.183098861837907, 3.819718634205488, 4.45633840657307, 4.7746482927568605, 4.45633840657307, 4.7746482927568605, 4.45633840657307, 3.819718634205488, 4.7746482927568605, 2.864788975654116, 2.864788975654116, 3.5014087480216975, 3.183098861837907]
% --- Power ---
PowerL = [169, 199, 192, 241, 199, 200, 252, 201, 200]
PowerD = [7.321127382227186, 7.321127382227186, 7.639437268410976, 6.684507609859605, 7.002817496043395, 6.684507609859605, 7.321127382227186, 7.002817496043395, 7.002817496043395]
% --- BananaCoaxial ---
BananaCoaxialL = [119, 120, 118, 120]
BananaCoaxialD = [6.366197723675814, 5.729577951308232, 4.7746482927568605, 5.092958178940651]
% --- CrocodileCoaxial ---
CrocodileCoaxialL = [118, 108, 130, 109, 139, 151, 151]
CrocodileCoaxialD = [5.411268065124442, 5.411268065124442, 3.5014087480216975, 5.092958178940651, 5.092958178940651, 3.183098861837907, 3.5014087480216975]
% --- RJ11DB89 ---
RJ11DB89L = [152]
RJ11DB89D = [5.411268065124442]
% --- USB ---
USBL = [180, 192, 201, 199]
USBD = [5.092958178940651, 4.7746482927568605, 4.7746482927568605, 4.7746482927568605]
% --- VGA ---
VGAL = [192]
VGAD = [7.321127382227186]
% --- DB9 ---
DB9L = [210, 196]
DB9D = [4.138028520389279, 4.7746482927568605]
% --- Ethernet ---
EthernetL = [203]
EthernetD = [5.729577951308232]
% --- Coaxial ---
CoaxialL = [129, 42, 53, 95]
CoaxialD = [5.411268065124442, 5.411268065124442, 5.411268065124442, 5.092958178940651]



%scatter(lengths, diameters, 'MarkerEdgeColor', [0,0,0]);
mdl = fitlm(lengths, diameters, 'VarNames', {'Length', 'Diameter'})
r = mdl.Residuals.Raw;
plot(mdl)
title('Cable Length vs Diameter',...
    'FontUnits','points',...
    'Interpreter', 'latex',...
    'FontWeight','bold',...
    'FontSize',18,...
    'FontName','Times')
ylabel({'Diameter ($mm)$'}, 'Interpreter', 'latex')
xlabel('Length ($cm$)', 'Interpreter', 'latex')
set(gca,...
    'FontSize',12);
ax = gca;
ax.Box = 'off';
print -depsc2 lengthVsDiameter.eps

cla
plot(lengths, mdl.Residuals.Raw, 'o')
title('Cable Length vs Residual',...
    'FontUnits','points',...
    'Interpreter', 'latex',...
    'FontWeight','bold',...
    'FontSize',18,...
    'FontName','Times')
legend(['Residual'])
ylabel({'Residual'}, 'Interpreter', 'latex')
xlabel('Length ($cm$)', 'Interpreter', 'latex')
%axis([0.01,0.05,0.21,0.22])
set(gca,...
    'FontSize',12);
ax = gca;
ax.Box = 'off';
print -depsc2 lengthVsDiameterResiduals.eps

%scatter(lengths, log(diameters), 'MarkerFaceColor', [0,0,1]);

% scatter(BananaL, BananaD, 'MarkerFaceColor', [1,0,0]);
% scatter(PowerL, PowerD, 'MarkerFaceColor', [0,0,0]);
% scatter(BananaCoaxialL, BananaCoaxialD, 'MarkerFaceColor', [0,1,0]);
% scatter(CrocodileCoaxialL, CrocodileCoaxialD, 'MarkerFaceColor', [0,0,1]);
% scatter(RJ11DB89L, RJ11DB89D, 'MarkerFaceColor', [1,1,0]);
% scatter(USBL, USBD, 'MarkerFaceColor', [0,1,1]);
% scatter(VGAL, VGAD, 'MarkerFaceColor', [1,0.5,0]);
% scatter(DB9L, DB9D, 'MarkerFaceColor', [0,1,0.5]);
% scatter(EthernetL, EthernetD, 'MarkerFaceColor', [0.5,0.5,0.5]);
% scatter(CoaxialL, CoaxialD, 'MarkerFaceColor', [0.8,0.8,0.8]);
%histogram2(lengths,diameters);

%Print to file

