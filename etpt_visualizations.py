"""
ETPT Visualization Suite
Complete code for all eight visualizations in the framework.

Requires: numpy, scipy, matplotlib, seaborn, networkx
Optional: pymc (for Bayesian visualization)

Author: S R Tulasi Krishna
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import networkx as nx
from scipy.integrate import odeint
import matplotlib.animation as animation

# =====================================================
# SHARED DATA: B and P vectors for all archetypes
# =====================================================
B_human   = np.array([0.95, 0.90, 0.40, 0.25, 0.98, 0.85, 0.00, 0.10, 0.30])
P_human   = np.array([0.0004, 0.33, 0.067, 0.85, 0.01, 0.05, 0.30, 0.00])

B_ant     = np.array([0.15, 0.30, 0.20, 0.05, 0.10, 0.20, 0.40, 0.05, 0.95])
P_ant     = np.array([0.00, 0.20, 0.02, 0.40, 0.00, 0.95, 0.05, 0.00])

B_bat     = np.array([0.20, 0.10, 0.85, 0.15, 0.30, 0.25, 0.95, 0.00, 0.40])
P_bat     = np.array([0.001, 0.40, 0.95, 0.30, 0.40, 0.20, 0.10, 0.00])

B_octopus = np.array([0.95, 0.30, 0.05, 0.40, 0.85, 0.90, 0.00, 0.85, 0.10])
P_octopus = np.array([0.0008, 0.85, 0.05, 0.95, 0.00, 0.40, 0.10, 0.10])

P_blind   = np.array([0.00, 0.00, 0.10, 0.95, 0.02, 0.07, 0.32, 0.00])

B_labels = ['manual', 'biped', 'vocal', 'strength', 'fine_motor',
            'grip', 'aerial', 'aquatic', 'collective']
P_labels = ['vis_EM', 'FOV', 'acoustic', 'tactile', 'magnetic',
            'olfact', 'baromet', 'electric']

# Coefficients for intensity term, per archetype
alpha_dict = {'Human': 0.45, 'Ant': 0.85, 'Bat': 0.30, 'Octopus': 0.60}
D_dict     = {'Human': 0.90, 'Ant': 0.70, 'Bat': 0.60, 'Octopus': 0.80}


# =====================================================
# VISUALIZATION 1: B⊗P matrix heatmap with annotations
# =====================================================
def viz_bp_matrix(B, P, B_labels, P_labels, title='Human B⊗P matrix'):
    """
    Plot the B⊗P tensor as an annotated heatmap.
    Each cell M_ij = B_i * P_j represents the strength of the
    (capability_i, perception_j) intersection — the potential 
    accessibility of technology at that intersection.
    
    Connection to ETPT: this is the structural object of the
    Mirror Rule. Non-zero cells define the achievable 
    technological domain; zero cells define the prohibited domain.
    """
    M = np.outer(B, P)  # 9×8 matrix
    
    fig, ax = plt.subplots(figsize=(10, 9))
    sns.heatmap(M, annot=True, fmt='.3f', cmap='magma',
                xticklabels=P_labels, yticklabels=B_labels,
                cbar_kws={'label': 'B_i × P_j'}, ax=ax,
                linewidths=0.4, linecolor='white')
    ax.set_title(title, fontsize=14, pad=15)
    ax.set_xlabel('Perception axis (P)', fontsize=12)
    ax.set_ylabel('Biological axis (B)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    return fig

# Usage:
# viz_bp_matrix(B_human, P_human, B_labels, P_labels).savefig('viz1_human_bp.png', dpi=200)
# viz_bp_matrix(B_human, P_blind, B_labels, P_labels, 
#               title='Blind-dominant human B⊗P').savefig('viz1_blind_bp.png', dpi=200)


# =====================================================
# VISUALIZATION 2: T_path surface for all four archetypes
# =====================================================
def viz_tpath_surfaces():
    """
    T_path(S, D) = ‖B⊗P‖ · D · (1 − exp(−αS)) plotted as a
    surface over the (S, D) plane for each archetype.
    
    Connection to ETPT: this surface IS the technological 
    trajectory of a civilization. Shape governed by α; 
    height by ‖B⊗P‖ · D.
    """
    S = np.linspace(0, 5, 50)
    D = np.linspace(0, 1, 50)
    S_grid, D_grid = np.meshgrid(S, D)
    
    archetypes = [
        ('Human',   B_human,   P_human,   alpha_dict['Human']),
        ('Ant',     B_ant,     P_ant,     alpha_dict['Ant']),
        ('Bat',     B_bat,     P_bat,     alpha_dict['Bat']),
        ('Octopus', B_octopus, P_octopus, alpha_dict['Octopus']),
    ]
    
    fig = plt.figure(figsize=(16, 12))
    for idx, (name, B, P, a) in enumerate(archetypes, start=1):
        M = np.outer(B, P)
        bp_norm = np.linalg.norm(M, 'fro')  # use Frobenius norm as scalar magnitude
        T = bp_norm * D_grid * (1 - np.exp(-a * S_grid))
        
        ax = fig.add_subplot(2, 2, idx, projection='3d')
        surf = ax.plot_surface(S_grid, D_grid, T, cmap='viridis',
                               alpha=0.9, edgecolor='none')
        ax.set_title(f'{name}  (α={a}, ‖B⊗P‖={bp_norm:.2f})', pad=10)
        ax.set_xlabel('Survival pressure S')
        ax.set_ylabel('Density D')
        ax.set_zlabel('T_path')
        ax.view_init(elev=25, azim=-60)
    
    plt.suptitle('T_path surfaces for the four archetypes', fontsize=15)
    plt.tight_layout()
    return fig

# viz_tpath_surfaces().savefig('viz2_tpath_surfaces.png', dpi=200)


# =====================================================
# VISUALIZATION 3: Bifurcation diagram (reclassification threshold)
# =====================================================
def viz_bifurcation(rho_c=143, P0=0.5, P_max=1.0, beta=1e-3, f=0.3,
                    t_values=[0, 10, 50, 200, 1000]):
    """
    P_i(t) as a function of input density ρ, at several training times.
    Demonstrates the bifurcation: below ρ_c, P stays at P0; 
    above ρ_c, P grows toward P_max.
    
    Connection to ETPT: this is the visual signature of 
    Equation 1's threshold-bifurcation structure.
    """
    rho = np.linspace(0, 600, 500)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    for t in t_values:
        excess = np.clip(rho - rho_c, 0, None)
        P_t = P_max - (P_max - P0) * np.exp(-beta * excess * f * t)
        # below threshold, P stays at P0
        P_t = np.where(rho < rho_c, P0, P_t)
        ax.plot(rho, P_t, label=f't = {t} hr', linewidth=2)
    
    ax.axvline(rho_c, color='red', linestyle='--', alpha=0.7,
               label=f'ρ_c = {rho_c} bits/cm²/s')
    ax.axhline(P_max, color='gray', linestyle=':', alpha=0.5,
               label='P_max')
    ax.axhline(P0, color='gray', linestyle=':', alpha=0.5,
               label='P₀ (baseline)')
    ax.set_xlabel('Input density ρ (bits/cm²/s)', fontsize=12)
    ax.set_ylabel('P_i(t)', fontsize=12)
    ax.set_title('Reclassification bifurcation in P-vector update', fontsize=14)
    ax.legend(loc='lower right')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig

# viz_bifurcation().savefig('viz3_bifurcation.png', dpi=200)


# =====================================================
# VISUALIZATION 4: Step response — Comfort Trap recovery
# =====================================================
def viz_comfort_trap_recovery():
    """
    T(t) following pressure shock S_shock applied at t = 10,
    plotted for a range of α values spanning archetypal species.
    
    Connection to ETPT: empirically demonstrates that species 
    with low α may fail to recover within civilizational 
    timescales — Equation 5.
    """
    t = np.linspace(0, 50, 500)
    t_0 = 10
    S_shock = 1.0
    T_max = 1.0
    T_pre = 0.05
    gamma = 1.0
    
    alphas = [0.05, 0.15, 0.30, 0.45, 0.60, 0.85]
    colors = plt.cm.plasma(np.linspace(0.15, 0.85, len(alphas)))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    for a, c in zip(alphas, colors):
        T = np.full_like(t, T_pre)
        mask = t > t_0
        tau = t[mask] - t_0
        T[mask] = T_max - (T_max - T_pre) * np.exp(-gamma * a * S_shock * tau)
        ax.plot(t, T, label=f'α = {a}', color=c, linewidth=2)
    
    ax.axvline(t_0, color='red', linestyle='--', alpha=0.6, label='Shock onset')
    ax.axhline(T_max, color='gray', linestyle=':', alpha=0.5)
    ax.set_xlabel('Time (generations)', fontsize=12)
    ax.set_ylabel('T(t)', fontsize=12)
    ax.set_title('Comfort Trap Recovery — Step Response', fontsize=14)
    ax.legend(loc='lower right')
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig

# viz_comfort_trap_recovery().savefig('viz4_recovery.png', dpi=200)


# =====================================================
# VISUALIZATION 5: P expansion phase portrait
# =====================================================
def viz_p_phase_portrait():
    """
    Phase portrait of (P, dP/dt) for the cortical reassignment ODE
    at fixed ρ above threshold. Shows trajectories converging 
    to P_max attractor.
    
    Connection to ETPT: the dynamical structure of Equation 1.
    """
    rho_c = 143
    P_max = 1.0
    beta = 0.005  # for visible dynamics on plot scale
    f = 0.3
    rho_values = [100, 150, 200, 300, 500]
    
    P_grid = np.linspace(0, 1, 30)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot dP/dt vs P for each rho
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(rho_values)))
    for rho, c in zip(rho_values, colors):
        excess = max(rho - rho_c, 0)
        dPdt = beta * excess * (P_max - P_grid) * f
        ax.plot(P_grid, dPdt, label=f'ρ = {rho}', color=c, linewidth=2)
    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.scatter([P_max], [0], color='red', s=100, zorder=5,
               label='Attractor P=P_max')
    ax.set_xlabel('P_i (perception value)', fontsize=12)
    ax.set_ylabel('dP_i/dt', fontsize=12)
    ax.set_title('Phase portrait of P-vector expansion', fontsize=14)
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig

# viz_p_phase_portrait().savefig('viz5_phase.png', dpi=200)


# =====================================================
# VISUALIZATION 6: Intelligibility Index network
# =====================================================
def intelligibility(B1, P1, B2, P2):
    """Cosine similarity of flattened B⊗P matrices."""
    M1 = np.outer(B1, P1).flatten()
    M2 = np.outer(B2, P2).flatten()
    num = np.dot(M1, M2)
    den = np.linalg.norm(M1) * np.linalg.norm(M2)
    return num / den if den > 0 else 0.0

def viz_intelligibility_network():
    """
    Network of civilizations with edge weights = I(C_i, C_j).
    Connection to ETPT: Equation 4 visualized.
    Wider/redder edges = more mutually intelligible.
    """
    archetypes = {
        'Human':   (B_human, P_human),
        'Ant':     (B_ant, P_ant),
        'Bat':     (B_bat, P_bat),
        'Octopus': (B_octopus, P_octopus),
        'Blind-H': (B_human, P_blind),
    }
    
    G = nx.Graph()
    names = list(archetypes.keys())
    for n in names:
        G.add_node(n)
    
    edges = []
    for i, n1 in enumerate(names):
        for n2 in names[i+1:]:
            B1, P1 = archetypes[n1]
            B2, P2 = archetypes[n2]
            I = intelligibility(B1, P1, B2, P2)
            G.add_edge(n1, n2, weight=I)
            edges.append((n1, n2, I))
    
    pos = nx.spring_layout(G, seed=42, k=2)
    weights = [G[u][v]['weight'] * 8 for u, v in G.edges()]
    edge_colors = [G[u][v]['weight'] for u, v in G.edges()]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue',
                           edgecolors='black', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
    edges_drawn = nx.draw_networkx_edges(
        G, pos, width=weights, edge_color=edge_colors,
        edge_cmap=plt.cm.plasma, edge_vmin=0, edge_vmax=1, ax=ax
    )
    
    # Label edges
    edge_labels = {(u, v): f'{G[u][v]["weight"]:.2f}' for u, v in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
                                 font_size=9, ax=ax)
    ax.set_title('Intelligibility network among civilizations\n(edge weight = cosine similarity of B⊗P)',
                 fontsize=13)
    ax.axis('off')
    plt.tight_layout()
    return fig, edges

# fig, edges = viz_intelligibility_network()
# fig.savefig('viz6_intelligibility.png', dpi=200)
# for e in edges: print(f"  {e[0]:8s}  ↔  {e[1]:8s}    I = {e[2]:.3f}")


# =====================================================
# VISUALIZATION 7: Technology Accessibility 3D terrain
# =====================================================
def viz_accessibility_terrain(theta=0.05, k=20):
    """
    A(i,j) plotted as a surface over (B_i, P_j) coordinates.
    Connection to ETPT: Equation 3 — emergence probability terrain.
    """
    B_axis = np.linspace(0, 1, 60)
    P_axis = np.linspace(0, 1, 60)
    Bg, Pg = np.meshgrid(B_axis, P_axis)
    
    # Sigmoidal accessibility, ignoring c_ij (set to 1 for shape)
    A = 1.0 / (1.0 + np.exp(-k * (Bg * Pg - theta)))
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(Bg, Pg, A, cmap='cividis',
                           alpha=0.9, edgecolor='none')
    ax.contour(Bg, Pg, A, zdir='z', offset=0, cmap='cividis', linestyles='solid')
    ax.set_xlabel('B_i')
    ax.set_ylabel('P_j')
    ax.set_zlabel('A(i,j)')
    ax.set_title(f'Technology Accessibility Function (θ={theta}, k={k})',
                 fontsize=14)
    fig.colorbar(surf, shrink=0.5, label='Accessibility')
    ax.view_init(elev=25, azim=-55)
    plt.tight_layout()
    return fig

# viz_accessibility_terrain().savefig('viz7_accessibility.png', dpi=200)


# =====================================================
# VISUALIZATION 8: Bayesian posterior update (termite mound)
# =====================================================
def viz_bayesian_update():
    """
    Static plot showing posterior mean ± credible interval 
    over selected B and P components after each artifact 
    feature is observed.
    Simplified MCMC-equivalent for demonstration.
    Connection to ETPT: Equation 6 — sequential reverse inference.
    """
    # Parameter indices we'll display
    components = ['B_manual', 'B_collective', 'P_visEM', 
                  'P_tactile', 'P_chemical', 'P_baromet']
    
    # Synthetic posterior trajectories: prior 0.5, mean tightens toward true value
    true_vals = [0.05, 0.95, 0.001, 0.85, 0.97, 0.70]
    
    features_observed = [
        'prior',
        'A1: passive vent',
        'A4: no center',
        'A7: pheromone',
        'A8: blind workers',
        'A3: scale ratio',
        'A10: insolation',
    ]
    n_steps = len(features_observed)
    
    means   = np.zeros((n_steps, len(components)))
    stds    = np.zeros((n_steps, len(components)))
    for i, true_val in enumerate(true_vals):
        # exponential convergence model for illustration
        means[:, i] = 0.5 + (true_val - 0.5) * (1 - np.exp(-0.6 * np.arange(n_steps)))
        stds[:, i]  = 0.3 * np.exp(-0.5 * np.arange(n_steps))
    
    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(n_steps)
    colors = plt.cm.tab10(np.linspace(0, 1, len(components)))
    for i, (comp, c) in enumerate(zip(components, colors)):
        ax.errorbar(x + 0.1*i, means[:, i], yerr=stds[:, i],
                    label=comp, color=c, marker='o', capsize=4, linewidth=1.5)
    
    ax.set_xticks(x)
    ax.set_xticklabels(features_observed, rotation=30, ha='right')
    ax.set_ylabel('Posterior mean (± 1σ)', fontsize=12)
    ax.set_title('Sequential Bayesian update — termite mound reverse inference',
                 fontsize=13)
    ax.set_ylim(-0.05, 1.05)
    ax.axhline(0.5, color='gray', linestyle=':', alpha=0.5, label='Prior mean')
    ax.legend(loc='center right', fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    return fig

# viz_bayesian_update().savefig('viz8_bayes.png', dpi=200)


# =====================================================
# Run-all driver
# =====================================================
def run_all():
    """Generate every figure in the suite."""
    viz_bp_matrix(B_human, P_human, B_labels, P_labels,
                  title='Human B⊗P').savefig('viz1a_human.png', dpi=200)
    viz_bp_matrix(B_human, P_blind, B_labels, P_labels,
                  title='Blind-dominant human B⊗P').savefig('viz1b_blind.png', dpi=200)
    viz_tpath_surfaces().savefig('viz2_surfaces.png', dpi=200)
    viz_bifurcation().savefig('viz3_bifurcation.png', dpi=200)
    viz_comfort_trap_recovery().savefig('viz4_recovery.png', dpi=200)
    viz_p_phase_portrait().savefig('viz5_phase.png', dpi=200)
    fig, edges = viz_intelligibility_network()
    fig.savefig('viz6_intelligibility.png', dpi=200)
    print('Intelligibility values:')
    for e in edges:
        print(f'  {e[0]:10s} ↔ {e[1]:10s}  I = {e[2]:.3f}')
    viz_accessibility_terrain().savefig('viz7_accessibility.png', dpi=200)
    viz_bayesian_update().savefig('viz8_bayes.png', dpi=200)
    print('All eight figures saved.')

if __name__ == '__main__':
    run_all()
