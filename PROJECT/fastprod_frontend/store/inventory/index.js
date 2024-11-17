export const state = () => ({
  devices: [],
  device: {},
});

export const mutations = {
  update(state, params) {
    state.device = { ...params };
  },
  updateDevices(state, params) {
    state.devices = [...params];
  },
};

export const actions = {
  get({ commit, state }, params) {
    console.log("===>", this.$axios);
    return this.$axios.get(`/devices`);
  },
  getByName({ commit, rootGetters }, params) {
    return this.$axios.get(`/devices/${params.name}`);
  },
  getFacts({ commit, rootGetters }, params) {
    return this.$axios.get(`/devices/${params.name}/facts`);
  },
  getInterfacesIp({ commit, rootGetters }, params) {
    return this.$axios.get(`/devices/${params.name}/interfaces/ip`);
  },
  getInterfaces({ commit, rootGetters }, params) {
    return this.$axios.get(`/devices/${params.name}/interfaces`);
  },
  getSnapshots({ commit, rootGetters }, params) {
    return this.$axios.get(`/devices/${params.name}/snapshots`);
  },
  buildSnapshots({ commit, rootGetters }, params) {
    return this.$axios.post(`/devices/${params.name}/snapshots`);
  },
  config({ commit, rootGetters }, params) {
    return this.$axios.post(`/devices/${params.name}/config`, params.data);
  },

  post({ commit }, params) {
    return this.$axios.post(`/devices`, params.data);
  },
  delete({ commit }, params) {
    return this.$axios.delete(`/devices/${params.name}`);
  },
};

export const getters = {
  get: (state) => {
    return state.device;
  },
  getDevices: (state) => {
    return state.devices;
  },
};
