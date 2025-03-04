# Re-import necessary libraries after execution state reset
m_pion = 139.57061
m_muo = 105.6583715

momentum = (m_pion**2 - m_muo**2)/(2*m_pion)
energy_muon = m_pion - momentum
e_kin = energy_muon - m_muo
print(momentum, energy_muon, e_kin)