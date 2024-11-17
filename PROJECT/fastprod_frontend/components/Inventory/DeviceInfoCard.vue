<template>
  <UiCard :title="deviceName" icon="server" :flat="false" v-if="!!item">
    <template #headerActions>
      <div class="text-center" v-show="!loading">
        <v-icon
          size="100"
          v-if="item.data.device_type === 'router'"
          color="primary"
          >mdi-router</v-icon
        >
        <v-icon size="100" v-else color="primary">mdi-border-outside</v-icon>
        <br />
        <span class="text-h5 text-center">{{ item.hostname }}</span>
      </div>
    </template>

    <template #content>
      <div class="text-center">
        <v-progress-circular
          :size="70"
          :width="7"
          color="primary"
          indeterminate
          v-show="loading"
        ></v-progress-circular>
      </div>
      <div v-show="!loading">
        <v-divider class="mb-4"></v-divider>
        <v-row justify="center" align="center" class="text-center">
          <v-col cols="3" class="text-capitalize">
            <v-icon color="primary"> mdi-map-marker-radius-outline </v-icon>
            <span class="font-weight-bold">Location :</span>
            {{ item.data.locality }}
          </v-col>
          <v-col lg="4" md="4" cols="12">
            <v-icon color="primary">
              mdi-office-building-marker-outline
            </v-icon>
            <span class="font-weight-bold">Building :</span>
            {{ item.data.building }}
          </v-col>
          <v-col lg="4" md="4" cols="12">
            <v-icon color="primary"> mdi-domain </v-icon>
            <span class="font-weight-bold">Room :</span>
            {{ item.data.room }}
          </v-col>
          <v-col lg="4" md="4" cols="12">
            <v-icon color="primary"> mdi-devices </v-icon>
            <span class="font-weight-bold">Type :</span>
            <span v-if="item.data.device_type == 'router'">Router</span>
            <span v-if="item.data.device_type == 'switch_router'">Router</span>
          </v-col>
          <v-col lg="4" md="4" cols="12">
            <v-icon color="primary"> mdi-cog-sync-outline </v-icon>
            <span class="font-weight-bold">Model :</span>
            {{ item.data.device_model }}
          </v-col>
          <v-col lg="4" md="4" cols="12">
            <v-icon color="primary"> mdi-cog-sync-outline </v-icon>
            <span class="font-weight-bold">OS :</span>
            <span class="text-capitalize">
              {{ item.groups[0] }}
            </span>
          </v-col>
        </v-row>
      </div>
    </template>
  </UiCard>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      default: null,
    },
    deviceName: {
      type: String,
      default: null,
    },
    loading: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {},
};
</script>
<style scoped></style>
